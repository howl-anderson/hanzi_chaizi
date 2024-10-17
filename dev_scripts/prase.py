import pickle
import pathlib

WORKSPACE_DIR = pathlib.Path(__file__).parent.parent

data = {}

for i in [
    WORKSPACE_DIR / "chaizi/chaizi-ft.txt",
    WORKSPACE_DIR / "chaizi/chaizi-jt.txt",
]:
    with open(i, "rt") as fd:
        for line in fd:
            item_list = line.strip().split("\t")
            key = item_list[0]
            value = [i.strip().split() for i in item_list[1:]]

            data[key] = value

output_file = WORKSPACE_DIR / "hanzi_chaizi/data/data.pkl"

with open(output_file, "wb") as fd:
    pickle.dump(data, fd)
