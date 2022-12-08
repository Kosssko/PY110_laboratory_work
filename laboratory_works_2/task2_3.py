from itertools import count

def pow_gen(base: int):
    a = 0
    while True:  # TODO записать функцию-генератор
        yield base ** a
        a += 1


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))
