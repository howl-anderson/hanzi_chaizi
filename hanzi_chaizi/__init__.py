import pickle

import pkg_resources


class HanziChaizi(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "data/data.pkl")

        with open(data_file, 'rb') as fd:
            self.data = pickle.load(fd)


    # 若输入的拆字为 "一" 这种不可拆的汉字时
    # 拆字结果以其自生为结果集
    # eg: input: 一
    #    output: ['一']
    def query(self, input_char, default=None):
        result = self.data.get(input_char, default)
        if result == None:
            return [input_char]
        else:
            return result[0]


if __name__ == "__main__":
    hc = HanziChaizi()
    result_1 = hc.query('名')
    result_2 = hc.query('一')
    result_3 = hc.query('之')

    print(result_1)
    print(result_2)
    print(result_3)