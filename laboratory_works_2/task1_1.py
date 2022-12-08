def task() -> int:
    list_words = [
        "Goldenrod",
        "Purple",
        "Salmon",
        "Turquoise",
        "Cyan"
    ]

    return len(max(word for word in list_words))  # TODO записать выражение-генератор


if __name__ == "__main__":
    print(task())


