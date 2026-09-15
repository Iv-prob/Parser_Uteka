from fastapi import FastAPI
from delivery_parser_my import get_books
app = FastAPI()


@app.get('/books')
def show_catalog():
    data = get_books()
    return data
