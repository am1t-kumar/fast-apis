from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> dict:
    return {"message": "Hello World!"}


books = [
    {"id": 1, "title": "Harry Potter", "author": "J.K. Rowling", "year": 1997},
    {
        "id": 2,
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "year": 1954,
    },
]


@app.get("/books")
async def get_books() -> dict:
    return {"books": books}


@app.post("/books")
async def add_book(book: dict) -> dict:
    books.append(book)
    return {"books": books, "message": "Book added successfully!"}


@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"books": books, "message": "Book deleted successfully!"}
    return {"message": "Book not found!"}


@app.put("/books/{book_id}")
async def update_book(book_id: int, book: dict) -> dict:
    for b in books:
        if b["id"] == book_id:
            b.update(book)
            return {"books": books, "message": "Book updated successfully!"}
    return {"message": "Book not found!"}
