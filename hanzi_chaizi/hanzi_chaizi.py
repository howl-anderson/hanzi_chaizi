import pickle
from importlib.resources import files


class HanziChaizi:
    data: dict[str, list[list[str]]]

    def __init__(self):
        data_file = files(__package__).joinpath("data/data.pkl")

        with data_file.open("rb") as fd:
            self.data = pickle.load(fd)

    def query(
        self, input_char: str, default: list[str] | None = None
    ) -> list[str] | None:
        result = self.data.get(input_char)
        if result is None:
            return default
        return result[0]
