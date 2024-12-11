# VERSION: 0.0.26
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

from utils.logger import setup_logger

class PrettyPrint:
    def __init__(self):
        # Inizializza una lista per salvare tutte le stringhe stampate
        self.dictionary_list = []
        self.logger = setup_logger(__name__)

    def __call__(self, dictionary): # *args, **kwargs):
        # Se serve comunque stampare l'dictionary_list, puoi usare:
        if 'link' in dictionary and 'name' in dictionary and 'size' in dictionary and 'seeds' in dictionary and 'leech' in dictionary and 'engine_url' in dictionary and 'desc_link' in dictionary:
            # convert size to bytes
            dictionary['size'] = self.__anySizeToBytes(dictionary['size'])
            dictionary['name'] = dictionary["name"].replace("|", " ")
            self.dictionary_list.append(dictionary)

    def __anySizeToBytes(self, size_string):
        """
        Convert a string like '1 KB' to '1024' (bytes)
        """
        # separate integer from unit
        try:
            size, unit = size_string.split()
        except:
            try:
                size = size_string.strip()
                unit = ''.join([c for c in size if c.isalpha()])
                if len(unit) > 0:
                    size = size[:-len(unit)]
            except:
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
        if type(self.dictionary_list) is list and len(self.dictionary_list) > 0:
            return self.dictionary_list
        else:
            return None

    def clear(self):
        # Resetta l'elenco delle stringhe salvate
        self.dictionary_list = []