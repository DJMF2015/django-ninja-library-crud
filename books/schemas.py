from ninja import Schema
from datetime import datetime


class BookSchema(Schema):
    id: int
    title: str
    author: str
    description: str
    year: int
    image: str
    created_at: datetime
    updated_at: datetime


class BookSchemaIn(Schema):
    title: str
    author: str
    description: str
    year: int
    image: str
