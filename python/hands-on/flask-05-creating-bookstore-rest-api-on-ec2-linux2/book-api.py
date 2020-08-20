# Import Flask modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Create an object named app
app = Flask(__name__)
# Configure sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./bookstore.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

# Write a function named `init_bookstore_db` which initializes the bookstore db
# Create books table within sqlite db and populate with sample data
# Execute the code below only once.
def init_bookstore_db():
    drop_table = 'DROP TABLE IF EXISTS books;'
    books_table = """
    CREATE TABLE books(
    book_id INTEGER PRIMARY KEY,
    title VARCHAR NOT NULL,
    author VARCHAR,
    is_sold BOOLEAN NOT NULL DEFAULT 0 CHECK(is_sold IN(0,1)));
    """
    data = """
    INSERT INTO books (title, author, is_sold)
    VALUES
        ("Where the Crawdads Sing", "Delia Owens", 1 ),
        ("The Vanishing Half: A Novel", "Brit Bennett", 0),
        ("1st Case", "James Patterson, Chris Tebbetts", 0);
    """
    db.session.execute(drop_table)
    db.session.execute(books_table)
    db.session.execute(data)
    db.session.commit()

# Write a function named `get_all_books` which gets all books from the books table in the db,
# and return result as list of dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': True or False} ]`.
def get_all_books():
    query = """
    SELECT * FROM books;
    """

    result = db.session.execute(query)
    books = [ {'book_id':row[0], 'title':row[1], 'author':row[2], 'is_sold': bool(row[3])}  for row in result]
    return books


# Write a function named `find_book` which finds book using book_id from the books table in the db,
# and return result as list of dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.

# Write a function named `insert_book` which inserts book into the books table in the db,
# and return the newly added book as dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.

# Write a function named `change_book` which updates book into the books table in the db,
# and return updated added book as dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.

# Write a function named `remove_book` which removes book from the books table in the db,
# and returns True if successfully deleted or False.

# Write a function named `home` which returns 'Welcome to the Callahan's Bookstore API Service',
# and assign to the static route of ('/')

# Write a function named `get_books` which returns all books in JSON format for `GET`,
# and assign to the static route of ('/books')

# Write a function named `get_books` which returns the book with given book_id in JSON format for `GET`,
# and assign to the static route of ('/books/<int:book_id>')

# Write a function named `add_book` which adds new book using `POST` methods,
# and assign to the static route of ('/books')

# Write a function named `update_book` which updates an existing book using `PUT` method,
# and assign to the static route of ('/books/<int:book_id>')

# Write a function named `delete_book` which updates an existing book using `DELETE` method,
# and assign to the static route of ('/books/<int:book_id>')

# Write a function named `not_found` for handling 404 errors which returns 'Not found' in JSON format.

# Write a function named `bad_request` for handling 400 errors which returns 'Bad Request' in JSON format.

# Add a statement to run the Flask application which can be reached from any host on port 80.