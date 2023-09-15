import os


BOOK_PATH = 'book\\book.txt'
PAGE_SIZE = 800

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    """
    A function that returns a string with the text of the page and its size
    """
    marks = ',.!:;?'
    marks_in_text = any(m in text for m in marks)

    if text and marks_in_text and (start < len(text)):
        if start + size >= len(text):
            part = text[start:]
        else:
            while ((text[start+size] in marks)
                   or (text[start+size-1] not in marks)):
                size -= 1
            part = text[start:start+size]
    else:
        part = ''
    return part, len(part)


def prepare_book(path: str) -> None:
    """
    The function that forms the dictionary of the book
    """
    with open(path, 'r', encoding='utf-8') as file:
        txt_book = file.read()
    start = 0
    page = 1
    part = _get_part_text(txt_book, start, PAGE_SIZE)
    while part[0] != '':
        book[page] = part[0].lstrip()
        start += part[1]
        page += 1
        part = _get_part_text(txt_book, start, PAGE_SIZE)


# Calling the prepare_book function to prepare a book from a text file
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
