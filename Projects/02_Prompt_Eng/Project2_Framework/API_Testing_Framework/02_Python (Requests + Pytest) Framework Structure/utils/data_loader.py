import json


class DataLoader:
    def __init__(self, path='data/testdata.json'):
        with open(path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)

    def get_payload(self, key):
        return self.data[key]
