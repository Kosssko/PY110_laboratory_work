import json


def task():
    filename = "input.json"
    with open(filename) as f:
        data_file = json.load(f) # TODO считать содержимое JSON файла

    gen_exr = (num["contains_improvement_appeals"] for num in data_file)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
