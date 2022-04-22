from typing import List
import strawberry

from schemas.graphql.Book import Book


@strawberry.type
class Author:
    id: int
    name: str
    books: List[Book]
