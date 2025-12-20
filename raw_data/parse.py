"""
Parse raw chaizi data files and generate the pickle data file.

Usage:
    uv run python raw_data/parse.py
"""

import pickle
import pathlib

RAW_DATA_DIR = pathlib.Path(__file__).parent
PROJECT_DIR = RAW_DATA_DIR.parent

data = {}

for filepath in [
    RAW_DATA_DIR / "chaizi-ft.txt",
    RAW_DATA_DIR / "chaizi-jt.txt",
]:
    with open(filepath, "rt", encoding="utf-8") as fd:
        for line in fd:
            item_list = line.strip().split("\t")
            key = item_list[0]
            value = [item.strip().split() for item in item_list[1:]]
            data[key] = value

output_file = PROJECT_DIR / "hanzi_chaizi/data/data.pkl"

with open(output_file, "wb") as fd:
    pickle.dump(data, fd)

print(f"Generated {output_file} with {len(data)} characters")
