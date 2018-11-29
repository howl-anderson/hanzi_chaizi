import pickle

data = {}

for i in ['chaizi/chaizi-ft.txt', 'chaizi/chaizi-jt.txt']:
    with open(i, 'rt') as fd:
        for line in fd:
            item_list = line.strip().split('\t')
            key = item_list[0]
            value = [i.strip().split() for i in item_list[1:]]

            data[key] = value

output_file = 'hanzi_chaizi/data/data.pkl'

with open(output_file, 'wb') as fd:
    pickle.dump(data, fd)

