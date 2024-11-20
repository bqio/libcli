from __future__ import annotations
from dataclasses import dataclass
from uuid import UUID
from enum import Enum


# book model
@dataclass
class Book:
    id: UUID
    title: str
    author: str
    year: int
    status: BookStatus

    def __str__(self):
        if self.status == 1:
            status = "в наличии"
        else:
            status = "выдана"
        return f"Book(id='{self.id}', title='{self.title}', author='{self.author}', year={self.year}, status='{status}')"


# book status model
class BookStatus(Enum):
    AVAILABLE = 1
    HANDED = 2
