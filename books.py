import yaml
from pydantic import BaseModel
from pydantic_core import to_jsonable_python

class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]

# Initialize the my_books list
my_books = [
    Book(
        author="J. K. Rowling",
        title="Harry Potter and the Philosopher's Stone",
        pages=[
            Page(number=1, text="There once was a boy..."),
            Page(number=2, text="He went to magic school...")
        ]
    ),
    Book(
        author="Edgar Allan Poe",
        title="The Complete Tales and Poems",
        pages=[
            Page(number=1, text="Book things pages words")
        ]
    )
]

# Convert one of the books into YAML
print("Single book in YAML format:")
print(yaml.dump(my_books[0].dict()))

# Convert the full list of books into YAML
print("Full list of books in YAML format:")
print(yaml.dump(to_jsonable_python(my_books)))
