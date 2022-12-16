import json


def task():
    filename = "input.json"
    with open(filename) as f:
        data_f = json.load(f)# TODO считать содержимое JSON файла

    return max(data_f, key= lambda x: x["score"])  # TODO найти максимальный элемент по ключу score


if __name__ == "__main__":
    print(task())
