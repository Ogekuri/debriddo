"""
@file src/debriddo/utils/novaprinter.py
@brief Module-level runtime logic and reusable symbols.
@details LLM-oriented Doxygen metadata for static analyzers and automated refactoring agents.
"""

# VERSION: 0.0.36
# AUTHORS: Ogekuri

# def prettyPrinter(dictionary):
#     dictionary['size'] = anySizeToBytes(dictionary['size'])
#     outtext = "|".join((dictionary["link"], dictionary["name"].replace("|", " "),
#                         str(dictionary["size"]), str(dictionary["seeds"]),
#                         str(dictionary["leech"]), dictionary["engine_url"]))
#     if 'desc_link' in dictionary:
#         outtext = "|".join((outtext, dictionary["desc_link"]))

#     # fd 1 is stdout
#     with open(1, 'w', encoding='utf-8', closefd=False) as utf8stdout:
#         print(outtext, file=utf8stdout)

from debriddo.utils.logger import setup_logger

class PrettyPrint:
    """
    @brief Class `PrettyPrint` encapsulates cohesive runtime behavior.
    @details Generated Doxygen block for class-level contract and extension boundaries.
    """
    def __init__(self):
        # Inizializza una lista per salvare tutte le stringhe stampate
        """
        @brief Execute `__init__` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__init__`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        self.dictionary_list = []
        self.logger = setup_logger(__name__)

    def __call__(self, dictionary): # *args, **kwargs):
        # Se serve comunque stampare l'dictionary_list, puoi usare:
        """
        @brief Execute `__call__` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `__call__`.
        @param dictionary Runtime input parameter consumed by `__call__`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if 'link' in dictionary and 'name' in dictionary and 'size' in dictionary and 'seeds' in dictionary and 'leech' in dictionary and 'engine_url' in dictionary and 'desc_link' in dictionary:
            # convert size to bytes
            dictionary['size'] = self.__anySizeToBytes(dictionary['size'])
            dictionary['name'] = dictionary["name"].replace("|", " ")
            self.dictionary_list.append(dictionary)

    def __anySizeToBytes(self, size_string):
        """
        @brief Execute `__anySizeToBytes` operational logic.
        @details Converts a human-readable size token into integer byte units using binary prefixes.
        @param self Runtime input parameter consumed by `__anySizeToBytes`.
        @param size_string Runtime input parameter consumed by `__anySizeToBytes`.
        @return Computed result payload; `-1` when parsing fails.
        @side_effect No external side effects.
        """
        # separate integer from unit
        try:
            size, unit = size_string.split()
        except ValueError:
            try:
                size = size_string.strip()
                unit = ''.join([c for c in size if c.isalpha()])
                if len(unit) > 0:
                    size = size[:-len(unit)]
            except Exception:
                return -1
        if len(size) == 0:
            return -1
        size = float(size)
        if len(unit) == 0:
            return int(size)
        short_unit = unit.upper()[0]

        # convert
        units_dict = {'T': 40, 'G': 30, 'M': 20, 'K': 10}
        if short_unit in units_dict:
            size = size * 2**units_dict[short_unit]
        return int(size)

    def get(self):
        # Restituisci l'elenco di tutte le stringhe accumulate
        """
        @brief Execute `get` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `get`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        if type(self.dictionary_list) is list and len(self.dictionary_list) > 0:
            return self.dictionary_list
        else:
            return None

    def clear(self):
        # Resetta l'elenco delle stringhe salvate
        """
        @brief Execute `clear` operational logic.
        @details Generated Doxygen block describing callable contract for LLM-native static reasoning.
        @param self Runtime input parameter consumed by `clear`.
        @return Computed result payload; `None` when side-effect-only execution path is selected.
        @side_effect May read/write process, network, filesystem, cache, or in-memory state depending on branch logic.
        """
        self.dictionary_list = []
