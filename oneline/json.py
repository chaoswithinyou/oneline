import json


class jsonOps:
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
