import json

from uuid import UUID
from enum import Enum
from pathlib import Path
from .models import Book, BookStatus


DB_PATH = Path("library.json")


# encoder for book serialization
class BookEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return obj.__dict__
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, Enum):
            return obj.value
        return json.JSONEncoder.default(self, obj)


def create_empty_db() -> None:
    with open(DB_PATH, "w", encoding="utf-8") as fp:
        json.dump(list(), fp)


# get all books
def read_books() -> list[Book]:
    if not DB_PATH.exists():
        create_empty_db()
    with open(DB_PATH, encoding="utf-8") as fp:
        contents: list[Book] = json.load(fp)
        books = [Book(**i) for i in contents]
        return books


# save book list
def write_books(books: list[Book]) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as fp:
        json.dump(books, fp, cls=BookEncoder)


# add new book
def db_add_book(book: Book) -> None:
    books = read_books()
    books.append(book)
    write_books(books)


# get all books
def db_get_books() -> list[Book]:
    return read_books()


# delete book by id
def db_del_book(id: UUID) -> None:
    books = read_books()
    founded = False
    for idx, book in enumerate(books):
        if str(book.id) == str(id):
            del books[idx]
            founded = True
    if not founded:
        raise Exception(f"ID {id} Not found")
    write_books(books)


# change book status by id
def db_change_book_status(id: UUID, status: BookStatus) -> None:
    books = read_books()
    founded = False
    for book in books:
        if str(book.id) == str(id):
            book.status = status
            founded = True
            print(book)
    if not founded:
        raise Exception(f"ID `{id}` Not found")
    write_books(books)


# search book by query
def db_search_book(query: str) -> Book | None:
    books = read_books()
    query = query.lower()
    for book in books:
        if (
            query in book.title.lower()
            or query in book.author.lower()
            or query in str(book.year)
        ):
            return book
    return None
