from typing import List

# from fastapi import Depends
import strawberry

from schemas.graphql.Author import Author
from schemas.graphql.Book import Book

# from services.AuthorService import AuthorService


@strawberry.type
class Query:
    @strawberry.field
    def author(self) -> List[Author]:
        return []

    @strawberry.field
    def book(self) -> List[Book]:
        return []
