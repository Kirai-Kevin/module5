from pydantic import BaseModel

class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]

my_books = [
    Book(
        author="J. K. Rowling",
        title="Harry Potter and the Philosopher's Stone",
        pages=[
            Page(
                number=1,
                text="There once was a boy...",
            ),
            Page(
                number=2,
                text="He went to magic school...",
            )
        ]
    ),
    Book(
        author="Roger Zelazny",
        title="Lord of Light",
        pages=[
            Page(
                number=1,
                text="It is said that fifty-three years ago...",
            )
        ]
    ),
    Book(
        author="Greg Mortenson and David Oliver Relin",
        title="Three Cups of Tea",
        pages=[
            Page(
                number=1,
                text="Here we drink three cups of tea to do business...",
            ),
            Page(
                number=2,
                text="The first cup of tea is for strangers...",
            )
        ]
    ),
]

print(my_books[0].author)
print(my_books[0].pages[0].text)

for book in my_books:
    print(book.title)
