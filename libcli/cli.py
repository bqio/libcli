import argparse
from uuid import uuid4, UUID

from .db import (
    db_add_book,
    db_get_books,
    db_del_book,
    db_change_book_status,
    db_search_book,
)
from .models import Book, BookStatus


# Cli commands
def add_book(args) -> None:
    book = Book(
        id=uuid4(),
        title=args.title,
        author=args.author,
        year=args.year,
        status=BookStatus.AVAILABLE,
    )
    db_add_book(book)


def del_book(args) -> None:
    db_del_book(id=args.id)


def change_book(args) -> None:
    if args.status == "в наличии":
        status = BookStatus.AVAILABLE
    elif args.status == "выдана":
        status = BookStatus.HANDED
    else:
        raise Exception(
            f"Status `{args.status}` not recognized. Use `в наличии` or `выдана`"
        )
    db_change_book_status(id=args.id, status=status)


def search_book(args) -> None:
    book = db_search_book(args.query)
    if book:
        print(book)
    else:
        print("Not found.")


def show_books(args) -> None:
    books = db_get_books()
    if len(books) == 0:
        return print("Books not found.")
    for book in books:
        print(book)


# main function/parse args
def main():
    main_parser = argparse.ArgumentParser(description="Library CLI")
    subcommands = main_parser.add_subparsers()

    add_parser = subcommands.add_parser("add", help="Add book")
    add_parser.add_argument("title", type=str, help="Book title")
    add_parser.add_argument("author", type=str, help="Book author")
    add_parser.add_argument("year", type=int, help="Book year")
    add_parser.set_defaults(func=add_book)

    delete_parser = subcommands.add_parser("delete", help="Delete book")
    delete_parser.add_argument("id", type=UUID, help="Book ID")
    delete_parser.set_defaults(func=del_book)

    change_parser = subcommands.add_parser("change", help="Change book status")
    change_parser.add_argument("id", type=UUID, help="Book ID")
    change_parser.add_argument("status", type=str, help="Book status")
    change_parser.set_defaults(func=change_book)

    search_parser = subcommands.add_parser("search", help="Search book")
    search_parser.add_argument("query", type=str, help="Search query")
    search_parser.set_defaults(func=search_book)

    show_parser = subcommands.add_parser("show", help="Show all books")
    show_parser.set_defaults(func=show_books)

    args = main_parser.parse_args()
    if "func" in args:
        args.func(args)
    else:
        print("Usage: libcli -h")
