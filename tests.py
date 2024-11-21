import unittest

from libcli.db import (
    db_add_book,
    db_change_book_status,
    db_del_book,
    db_get_books,
    db_search_book,
    create_empty_db,
)
from libcli.models import Book, BookStatus
from uuid import uuid4


class TestCli(unittest.TestCase):
    def test_add_book(self):
        create_empty_db()
        books = db_get_books()
        current_length = len(books)
        book = Book(
            id=uuid4(),
            title="TestBook",
            author="TestAuthor",
            year=1998,
            status=BookStatus.AVAILABLE,
        )
        db_add_book(book)
        books = db_get_books()
        self.assertEqual(current_length + 1, len(books))

    def test_del_book(self):
        create_empty_db()
        book = Book(
            id=uuid4(),
            title="TestBook",
            author="TestAuthor",
            year=1998,
            status=BookStatus.AVAILABLE,
        )
        db_add_book(book)
        db_del_book(id=book.id)
        books = db_get_books()
        self.assertEqual(len(books), 0)

    def test_change_book(self):
        create_empty_db()
        book = Book(
            id=uuid4(),
            title="TestBook",
            author="TestAuthor",
            year=1998,
            status=BookStatus.AVAILABLE,
        )
        db_add_book(book)
        db_change_book_status(book.id, BookStatus.HANDED)
        book = db_search_book("Test")
        self.assertEqual(book.status, BookStatus.HANDED.value)

    def test_search_book(self):
        create_empty_db()
        book = Book(
            id=uuid4(),
            title="TestBook",
            author="TestAuthor",
            year=1998,
            status=BookStatus.AVAILABLE,
        )
        db_add_book(book)
        book2 = db_search_book("Test")
        self.assertEqual(str(book.id), str(book2.id))


if __name__ == "__main__":
    unittest.main()
