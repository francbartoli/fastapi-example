from typing import List
import strawberry


@strawberry.type
class Book:
    id: int
    name: str
