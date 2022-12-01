def task() -> list:
    temp_tuple = (0, 36.6, 100)
    const_1 = 1.8
    const_2 = 32
    return list(map(lambda x: (x * const_1) + const_2, temp_tuple))  # TODO  вернуть список температур по Фаренгейту


if __name__ == "__main__":
    print(task())
