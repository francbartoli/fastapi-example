from typing import List, Optional

from fastapi import APIRouter, Depends, status

from schemas.AuthorSchema import (
    AuthorPostRequestSchema,
    AuthorSchema,
)
from schemas.BookSchema import BookSchema
from services.AuthorService import AuthorService

AuthorRouter = APIRouter(
    prefix="/v1/authors", tags=["author"]
)


@AuthorRouter.get("/", response_model=List[AuthorSchema])
def index(
    name: Optional[str] = None,
    pageSize: Optional[int] = 100,
    startIndex: Optional[int] = 0,
    authorService: AuthorService = Depends(),
):
    return authorService.list(name, pageSize, startIndex)


@AuthorRouter.get("/{id}", response_model=AuthorSchema)
def get(id: int, authorService: AuthorService = Depends()):
    return authorService.get(id)


@AuthorRouter.post(
    "/",
    response_model=AuthorSchema,
    status_code=status.HTTP_201_CREATED,
)
def create(
    author: AuthorPostRequestSchema,
    authorService: AuthorService = Depends(),
):
    return authorService.create(author)


@AuthorRouter.put("/{id}", response_model=AuthorSchema)
def update(
    id: int,
    author: AuthorPostRequestSchema,
    authorService: AuthorService = Depends(),
):
    return authorService.update(id, author)


@AuthorRouter.delete(
    "/{id}", status_code=status.HTTP_204_NO_CONTENT
)
def delete(
    id: int, authorService: AuthorService = Depends()
):
    return authorService.delete(id)


@AuthorRouter.get(
    "/{id}/books/", response_model=List[BookSchema]
)
def get_books(
    id: int, authorService: AuthorService = Depends()
):
    return authorService.get_books(id)
