#!/usr/bin/env bash
## @file doxygen.sh
## @brief Generate Doxygen documentation artifacts for src/ in HTML, PDF, and Markdown.
## @details Builds Doxygen config at runtime, generates HTML+LaTeX+XML, compiles PDF from LaTeX, then derives Markdown from Doxygen XML.

set -euo pipefail

## @brief Resolve repository root and output directories.
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
OUTPUT_ROOT="${PROJECT_ROOT}/doxygen"
HTML_DIR="${OUTPUT_ROOT}/html"
PDF_DIR="${OUTPUT_ROOT}/pdf"
PDF_LATEX_DIR="${PDF_DIR}/latex"
MARKDOWN_DIR="${OUTPUT_ROOT}/markdown"

## @brief Fail with explicit message and non-zero exit code.
## @param $1 Error message.
fail() {
  printf 'ERROR: %s\n' "$1" >&2
  exit 1
}

command -v doxygen >/dev/null 2>&1 || fail "doxygen command not found in PATH"
command -v make >/dev/null 2>&1 || fail "make command not found in PATH"

rm -rf "${OUTPUT_ROOT}"
mkdir -p "${HTML_DIR}" "${PDF_DIR}" "${MARKDOWN_DIR}"

CONFIG_FILE="$(mktemp /tmp/debriddo-doxygen.XXXXXX)"
cleanup() {
  rm -f "${CONFIG_FILE}"
}
trap cleanup EXIT

cat > "${CONFIG_FILE}" <<CFG
PROJECT_NAME           = "Debriddo"
PROJECT_BRIEF          = "Generated API documentation"
OUTPUT_DIRECTORY       = ${OUTPUT_ROOT}
CREATE_SUBDIRS         = NO
ALLOW_UNICODE_NAMES    = YES
OUTPUT_LANGUAGE        = English
MARKDOWN_SUPPORT       = YES
AUTOLINK_SUPPORT       = YES
BUILTIN_STL_SUPPORT    = YES
EXTRACT_ALL            = YES
EXTRACT_PRIVATE        = YES
EXTRACT_STATIC         = YES
EXTRACT_LOCAL_CLASSES  = YES
EXTRACT_LOCAL_METHODS  = YES
HIDE_UNDOC_MEMBERS     = NO
HIDE_UNDOC_CLASSES     = NO
HIDE_SCOPE_NAMES       = NO
SHOW_INCLUDE_FILES     = NO
INLINE_INFO            = YES
SORT_MEMBER_DOCS       = YES
SORT_BRIEF_DOCS        = YES
SORT_BY_SCOPE_NAME     = YES
RECURSIVE              = YES
INPUT                  = ${PROJECT_ROOT}/src
FILE_PATTERNS          = *.py *.js *.html *.css
EXCLUDE_SYMLINKS       = YES
GENERATE_HTML          = YES
HTML_OUTPUT            = html
HTML_DYNAMIC_MENUS     = YES
GENERATE_TREEVIEW      = YES
GENERATE_LATEX         = YES
LATEX_OUTPUT           = pdf/latex
USE_PDFLATEX           = YES
PDF_HYPERLINKS         = YES
LATEX_BATCHMODE        = YES
GENERATE_XML           = YES
XML_OUTPUT             = xml
GENERATE_DOCSET        = NO
GENERATE_MAN           = NO
GENERATE_RTF           = NO
GENERATE_PERLMOD       = NO
QUIET                  = YES
WARN_IF_UNDOCUMENTED   = NO
WARN_IF_DOC_ERROR      = YES
WARN_NO_PARAMDOC       = NO
CFG

printf 'Generating Doxygen HTML/LaTeX/XML...\n'
doxygen "${CONFIG_FILE}"

if [ ! -f "${PDF_LATEX_DIR}/Makefile" ]; then
  fail "Doxygen LaTeX Makefile not generated"
fi

printf 'Generating PDF from LaTeX...\n'
if ! make -C "${PDF_LATEX_DIR}" >/dev/null 2>&1; then
  printf 'WARNING: LaTeX exited non-zero; validating PDF artifact...\n' >&2
fi
if [ ! -f "${PDF_LATEX_DIR}/refman.pdf" ]; then
  fail "PDF generation failed: refman.pdf not found"
fi
cp -f "${PDF_LATEX_DIR}/refman.pdf" "${PDF_DIR}/refman.pdf"

printf 'Generating Markdown from Doxygen XML...\n'
PYTHON_SCRIPT="$(mktemp /tmp/debriddo-doxygen-md.XXXXXX.py)"
cat > "${PYTHON_SCRIPT}" <<'PY'
import os
import xml.etree.ElementTree as ET

output_root = os.environ["OUTPUT_ROOT"]
xml_dir = os.path.join(output_root, "xml")
md_dir = os.environ["MARKDOWN_DIR"]
os.makedirs(md_dir, exist_ok=True)

for name in os.listdir(md_dir):
    if name.endswith(".md"):
        os.remove(os.path.join(md_dir, name))

def flatten_text(node):
    if node is None:
        return ""
    return " ".join("".join(node.itertext()).split())

entries = []
index = ET.parse(os.path.join(xml_dir, "index.xml")).getroot()
for compound in index.findall("compound"):
    refid = compound.attrib.get("refid", "")
    kind = compound.attrib.get("kind", "")
    name = flatten_text(compound.find("name"))
    if not refid or not name:
        continue
    xml_file = os.path.join(xml_dir, f"{refid}.xml")
    if not os.path.exists(xml_file):
        continue

    root = ET.parse(xml_file).getroot()
    compounddef = root.find("compounddef")
    brief = flatten_text(compounddef.find("briefdescription")) if compounddef is not None else ""
    detail = flatten_text(compounddef.find("detaileddescription")) if compounddef is not None else ""

    safe_name = refid.replace("/", "_")
    md_file = os.path.join(md_dir, f"{safe_name}.md")
    with open(md_file, "w", encoding="utf-8") as fh:
        fh.write(f"# {name}\n\n")
        fh.write(f"- kind: `{kind}`\n")
        fh.write(f"- refid: `{refid}`\n")
        fh.write(f"- brief: `{brief or 'N/A'}`\n")
        fh.write(f"- details: `{detail or 'N/A'}`\n\n")
        fh.write("## Members\n\n")
        if compounddef is not None:
            members = compounddef.findall(".//memberdef")
        else:
            members = []
        if not members:
            fh.write("- none\n")
        else:
            for member in members:
                m_kind = member.attrib.get("kind", "")
                m_name = flatten_text(member.find("name"))
                m_brief = flatten_text(member.find("briefdescription"))
                fh.write(f"- `{m_kind}` `{m_name}` :: `{m_brief or 'N/A'}`\n")

    entries.append((name, os.path.basename(md_file)))

entries.sort(key=lambda item: item[0].lower())
with open(os.path.join(md_dir, "index.md"), "w", encoding="utf-8") as idx:
    idx.write("# Doxygen Markdown Index\n\n")
    idx.write("Generated from Doxygen XML output.\n\n")
    for name, filename in entries:
        idx.write(f"- [{name}]({filename})\n")
PY

OUTPUT_ROOT="${OUTPUT_ROOT}" MARKDOWN_DIR="${MARKDOWN_DIR}" python3 "${PYTHON_SCRIPT}"
rm -f "${PYTHON_SCRIPT}"

[ -f "${HTML_DIR}/index.html" ] || fail "HTML output missing: ${HTML_DIR}/index.html"
[ -f "${PDF_DIR}/refman.pdf" ] || fail "PDF output missing: ${PDF_DIR}/refman.pdf"
ls "${MARKDOWN_DIR}"/*.md >/dev/null 2>&1 || fail "Markdown output missing under ${MARKDOWN_DIR}"

printf 'Documentation generated successfully in %s\n' "${OUTPUT_ROOT}"
