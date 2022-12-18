import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = (r"""#{4}\s(?P<position>\w+)\.\s+\[(?P<book>.+?)\]\((?P<book_url>https\W+amzn.to/\w+)\)\s+by\s+(?P<author>.+?)\s\W+(?P<recommended>[0-9]+\W\w+\%)\s+recommended\)\s+\W+(?P<cover_url>https://www.daolf.com/images(?:.\w+){4}).+\s+\"(?P<description>.+\s+.+\s+.+)\" """)

# positions:	#{4}\s(?P<position>\w+)
# book:		    \.\s+\[(?P<book>.+?)\]
# book_url:	    \((?P<book_url>https\W+amzn.to/\w+)\)
# author:		\s+by\s+(?P<author>.+?)\s+
# recommended:	\s\W+(?P<recommended>[0-9]+\W\w+\%)\s+recommended\)
# cover_url:	\s+\W+(?P<cover_url>https://www.daolf.com/images(?:.\w+){4}).+
# description:	\s+\"(?P<description>.+\s+.+\s+.+)\"

def task():
    book_pattern = re.compile(BOOK_REGEX)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
