import json
from random import shuffle


def save_json(data, path):
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Saved json file at: {path}")
    except Exception as e:
        print(e)


def load_json(path):
    try:
        with open(path) as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(e)

class jsonWrapper:
    def __init__(self, json_path) -> None:
        try:
            with open(json_path) as f:
                self.data = json.load(f)
        except Exception as e:
            print(e)

    def __len__(self):
        return len(self.data)

    def getKeys(self):
        return self.data.keys()

    def __getitem__(self, index):
        return self.data[index]

    def split_train_val(self, train_propotion: float = 0.8, shuffel: bool = True):
        if shuffle:
            for i in range(10):
                shuffle(self.data)
        train_limit = train_propotion * len(self.data)
        train = self.data[: int(train_limit)]
        val = self.data[int(train_limit) :]

        print(f"Shuffle: {shuffel}")
        print(f"Length of training data: {len(train)}")
        print(f"Length of validation data: {len(val)}")

        return train, val
