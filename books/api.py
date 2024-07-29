from ninja import NinjaAPI
from .models import Book
from .schemas import BookSchema
from .schemas import BookSchemaIn
from django.shortcuts import get_object_or_404
from typing import List

api = NinjaAPI()  # create an instance of NinjaAPI


@api.get("/books", response=List[BookSchema])
def list_books(request):
    return Book.objects.filter(user=request.user).all()


@api.get("/books/{book_id}", response=BookSchema)
def get_book(request, book_id: int):
    return get_object_or_404(Book, id=book_id, user=request.user)


@api.post("/books", response=BookSchema)
def create_book(request, book: BookSchemaIn):
    book_obj = Book.objects.create(**book.dict(), user=request.user)
    return book_obj


@api.put("/books/{book_id}", response=BookSchema)
def update_book(request, book_id: int, data: BookSchemaIn):
    book_obj = get_object_or_404(Book, id=book_id, user=request.user)
    for attr, value in data.dict().items():
        setattr(book_obj, attr, value)
    book_obj.save()
    return book_obj


@api.delete("/books/{book_id}")
def delete_book(request, book_id: int):
    book_obj = get_object_or_404(Book, id=book_id, user=request.user)
    book_obj.delete()
    return {"success": True}
