"""
@file src/debriddo/check_unused_requirements.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.37
# AUTHORS: Ogekuri

import os
import ast
import importlib.metadata

def get_imported_modules_from_file(filepath):
    """@brief Function `get_imported_modules_from_file` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param filepath Runtime parameter.
"""
    imported_modules = set()
    with open(filepath, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read(), filename=filepath)
        except SyntaxError:
            return imported_modules

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                top_module = alias.name.split('.')[0].lower()  # forziamo minuscolo
                imported_modules.add(top_module)
        elif isinstance(node, ast.ImportFrom):
            if node.module is not None:
                top_module = node.module.split('.')[0].lower()  # forziamo minuscolo
                imported_modules.add(top_module)
    return imported_modules

def get_all_imported_modules(root_dir):
    """@brief Function `get_all_imported_modules` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param root_dir Runtime parameter.
"""
    all_imports = set()
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Ignora virtual env
        if '.venv' in dirnames:
            dirnames.remove('.venv')

        for filename in filenames:
            if filename.endswith('.py'):
                filepath = os.path.join(dirpath, filename)
                all_imports.update(get_imported_modules_from_file(filepath))
    return all_imports

def get_requirements(requirements_file):
    """@brief Function `get_requirements` runtime contract.
@details LLM-oriented operational contract for static analyzers and refactoring agents.
@param requirements_file Runtime parameter.
"""
    packages = set()
    with open(requirements_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            # estrai il nome del pacchetto senza versione
            pkg = line.split('=', 1)[0].split('<', 1)[0].split('>', 1)[0].strip().lower()  # minuscolo
            if pkg:
                packages.add(pkg)
    return packages

if __name__ == "__main__":
    root_dir = "."
    requirements_file = "requirements.txt"

    if not os.path.isfile(requirements_file):
        print("Non è presente requirements.txt nella directory corrente.")
        exit(1)

    imported_modules = get_all_imported_modules(root_dir)
    # imported_modules ora contiene solo minuscole

    required_packages = get_requirements(requirements_file)
    # required_packages ora contiene i nomi dei pacchetti in minuscolo

    pkg_to_distributions = importlib.metadata.packages_distributions()
    # pkg_to_distributions ha una struttura:
    # { "bs4": ["beautifulsoup4"], "apscheduler": ["APScheduler"], ... }

    # Invertiamo il mapping in modo da ottenere distribution -> {top_modules}
    distribution_to_top_modules = {}
    for top_mod, dists in pkg_to_distributions.items():
        top_mod_lower = top_mod.lower()
        for d in dists:
            d_lower = d.lower()
            if d_lower not in distribution_to_top_modules:
                distribution_to_top_modules[d_lower] = set()
            distribution_to_top_modules[d_lower].add(top_mod_lower)

    unused = []
    for pkg in required_packages:
        top_modules = distribution_to_top_modules.get(pkg, set())
        # Se non troviamo moduli top-level per questo pacchetto, supponiamo che il modulo top-level coincida con il nome del pacchetto
        if not top_modules:
            top_modules = {pkg}

        # Controlliamo se almeno uno dei top_modules è stato importato
        if not any(tm in imported_modules for tm in top_modules):
            unused.append(pkg)

    if unused:
        print("Pacchetti in requirements.txt non importati (considerando mapping top-level modules):")
        for u in sorted(unused):
            print(f" - {u}")
    else:
        print("Tutti i pacchetti in requirements.txt sembrano essere utilizzati.")
