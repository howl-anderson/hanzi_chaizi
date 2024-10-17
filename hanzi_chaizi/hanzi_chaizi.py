import pickle

import pkg_resources


class HanziChaizi(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "data/data.pkl")

        with open(data_file, "rb") as fd:
            self.data = pickle.load(fd)

    def query(self, input_char, default=None):
        result = self.data.get(input_char, default)
        return result[0]
