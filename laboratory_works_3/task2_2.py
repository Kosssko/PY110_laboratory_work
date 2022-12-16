import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename) as f_input:
        a = json.load(f_input)  # TODO считать содержимое json файл input.json

    with open(output_filename, "w") as f_output:  # TODO записать содержимое в json файл output.json с отступами
        json.dump(a, f_output, indent=4)

if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
