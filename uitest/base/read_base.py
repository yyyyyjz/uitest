import json


def read(path):
    with open("D:/uitest/data/" + path, "r", encoding="utf-8") as f:
        dict1 = json.load(f)
        list_data = []
        for value in dict1.values():
            list_data.append(value)
        return list_data