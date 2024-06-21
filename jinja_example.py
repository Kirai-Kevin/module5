import jinja2

env = jinja2.Environment()

template = env.from_string("Hi {{ their_name }}, my name is {{ my_name }}.")
print(template.render(their_name="John", my_name="Mary"))

# Add a fruit to the list and rerender the string
template = env.from_string("""
My favorite fruits are:
{% for fruit in fruits -%}
- {{ fruit }}
{% endfor %}
""")
print(template.render(fruits=["apples", "oranges", "bananas"]))

# Remove the `-` at the end of the `{% for fruit in fruits -%}` line
template = env.from_string("""
My favorite fruits are:
{% for fruit in fruits %}
- {{ fruit }}
{% endfor %}
""")
print(template.render(fruits=["apples", "oranges", "bananas"]))

# Initialize the `my_books` list
my_books = [
    {
        "author": "J. K. Rowling",
        "title": "Harry Potter and the Philosopher's Stone",
        "pages": [
            {"number": 1, "text": "There once was a boy..."},
            {"number": 2, "text": "He went to magic school..."}
        ]
    },
    {
        "author": "Edgar Allan Poe",
        "title": "The Complete Tales and Poems",
        "pages": [
            {"number": 1, "text": "Book things pages words"}
        ]
    }
]

template = env.from_string("""
The titles of my books are:
{% for book in books %}
- {{ book.title }}
{% endfor %}
""")
print(template.render(books=my_books))
