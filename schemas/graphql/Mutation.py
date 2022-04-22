from typing import List

import strawberry

from schemas.graphql.Author import Author
from schemas.graphql.Book import Book


@strawberry.type
class Mutation:
    @strawberry.field
    def add_author(
        self, name: str, books: List[Book]
    ) -> Author:
        return {}

    @strawberry.field
    def add_book(self, name: str) -> Book:
        return {}
