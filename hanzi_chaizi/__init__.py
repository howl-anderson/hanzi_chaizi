import pickle

import pkg_resources


class HanziChaizi(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "data/data.pkl")

        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)

    def query(self, input_char, default=None, char_type=0):
        '''
        Query the chaizi of a Chinese character.
        :param input_char: The Chinese character to query. It should be a single character.
        :param default: The default value to return if the input character is not found.
        '''
        result = self.data.get(input_char, default)
        res = result[char_type] if len(result) > char_type else result[0]
        res = res if res else input_char
        return res


if __name__ == "__main__":
    hc = HanziChaizi()
    result = hc.query('冰', char_type=1)

    print(result)
