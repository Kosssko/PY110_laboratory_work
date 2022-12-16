INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE) as f_input:  # TODO перезаписать содержимое одного файла в другой
        with open(OUTPUT_FILE, "w") as f_output:
            for line in map(str.upper, f_input):
                f_output.write(line)

if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")