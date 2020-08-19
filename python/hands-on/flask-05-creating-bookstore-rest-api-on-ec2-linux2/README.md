# Hands-on Flask-05 : Creating REST API (Bookstore Application) with Flask Framework

Purpose of the this hands-on training is to give students basic understanding of REST API and demonstrate how to create API using sqlite with Flask web application on Amazon Linux 2 EC2 instance.

![REST API Methods](./http-methods-flask.png)

## Learning Outcomes

At the end of the this hands-on training, students will be able to;

- demonstrate their knowledge of installing Python and Flask framework on Amazon Linux 2 EC2 instance.

- apply knowledge of building a web application with Python Flask framework.

- understand the basics of REST API architecture.

- design and implement REST API with Python Flask framework.

- configure connection to the `sqlite` database.

- work with a database using the SQL within Flask application.

- use git repo to manage the application versioning.

- run the web application on AWS EC2 instance using the GitHub repo as codebase.

## Outline

- Part 1 - Getting to know REST API

- Part 2 - Creating REST API Implementation with Flask framework using `sqlite` database on GitHub Repo

- Part 3 - Deploying the REST API Implementation with Flask Server on Amazon Linux 2 EC2 Instance

- Part 4 - Testing the API Implementation on EC2 Instance

## Part 1 - Getting to know REST API

[REST (REpresentational State Transfer)](https://en.wikipedia.org/wiki/Representational_state_transfer) is a software architectural style that defines a set of constraints to be used for creating Web services.

Features of a REST architecture can be defined as followings:

- **Client-Server:** The server offers a service, and the client consumes it.

- **Stateless:** The server does not have to remember previous requests from the client, in other words the server does not keep the session information of the client.

- **Cacheable:** The server must indicate to the clients and intermediaries if requests can be cached or not.

- **Uniform Interface:** The uniform interface is the fundamental of RESTful Services and simplifies the communication between the Server and Client.

- **Layered System:** A client does not know whether it communicates with the end server, or with an intermediary along the way. Besides, a server can send requests to the multiple other servers/microservices to generate a response.

- **Code on demand (optional):** Servers can optionally provide executable code or scripts to clients in their context.

![REST API Methods](./rest-api-methods.png)

Web services that conform to the REST architectural style, called **RESTful Web service** or **Web API (Application Programming Interface)** and designed to fit the Hypertext Transfer Protocol (HTTP).

Within the Web APIs, resources are represented by [URI (Uniform Resource Identifier)](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier). The clients send requests to the server using URIs with the HTTP methods `GET`, `POST`, `PUT`, and `DELETE` and the Server send response with data in any media type but JSON format is the most commonly used one in the market.

Within this hands-on, we will create a `Bookstore` Application as Web Service.  Below table shows the standard implementation of REST API for the `Bookstore` app and how the HTTP methods are designed to affect the given resources identified by URIs.

| HTTP Method  | Action | Example|
| --- | --- | --- |
| `GET`     |   Obtain information about a resource | http://api.example.com/books (retrieves list of all books) |
| `GET`     |   Obtain information about a resource | http://api.example.com/books/123 (retrieves book with id=123) |
| `POST`    |   Create a new resource               | http://api.example.com/books (creates a new book, from data provided with the request) |
| `PUT`     |   Update a resource                   | http://api.example.com/books/123 (updates the book with id=123, from data provided with the request) |
| `DELETE`  |   Delete a resource                   | http://api.example.com/books/123 (delete the book with id=123) |

## Part 2 - Creating REST API Implementation with Flask framework using `sqlite` database on GitHub Repo

- Create a `Bookstore` application as web service with base URL of `http://[public-dns-name-of-ec2]/` and expose the resources listed above within.

- Define a book with following fields:

  - book_id: unique identifier for books, type is numeric.

  - title: title of the book, type is string.

  - author: author of the book. type is string.

  - is_sold: book availability status, type is boolean.

- Create folder named `flask-04-creating-rest-api-on-ec2-linux2` within `clarusway-python-workshop` repo

- Write an REST API application using `sqlite` database and save the complete code as `book-api.py` under `hands-on/flask-04-creating-rest-api-on-ec2-linux2` folder.

```python
# Import Flask modules

# Create an object named app

# Configure sqlite database

# Write a function named `init_bookstore_db` which initializes the bookstore db
# Create books table within sqlite db and populate with sample data
# Execute the code below only once.

# Write a function named `get_all_books` which gets all books from the books table in the db,
# and return result as list of dictionary
# `[{'book_id': 1, 'title':'XXXX', 'author': 'XXXXXX', 'is_sold': 'Yes' or 'No'} ]`.

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

```

- Add and commit all changes on local repo

```bash
```

- Push all the files to remote repo `clarusway-python-workshop` on GitHub.

```bash
```

## Part 3 - Deploying the REST API Implementation with Flask Server on Amazon Linux 2 EC2 Instance

- Launch an Amazon EC2 instance using the Amazon Linux 2 AMI with security group allowing SSH (Port 22) and HTTP (Port 80) connections.

- Connect to your instance with SSH.

```bash
```

- Update the installed packages and package cache on your instance.

```bash
```

- Install `Python 3` packages.

```bash
```

- Check the python3 version

```bash
```

- Install `Python 3 Flask` framework.

```bash
```

- Install `flask_sqlalchemy`.

```bash
```

## Part 4 - Testing the API Implementation on EC2 Instance

- Download the web application file from GitHub repo.

```bash
```

- Run the `Bookstore` API.

```bash
```

- Open the `Bookstore` API from the web browser.

```bash
```

- Open the `Bookstore` API default `/` page from the terminal with `curl` command.

```bash
```

- List all book in  the `Bookstore` API using `/books` path and HTTP `GET` method with `curl` command.

```bash
```

- Retrieve book with `id=3` using `/books/3` path and HTTP `GET` method with `curl` command.

```bash
```

- Try to retrieve non-existing book using `/books/10` path and HTTP `GET` method with `curl` command to see 404 response.

```bash
```

- Create new book the `Bookstore` using `/books` path and HTTP `POST` method with `curl` command.

```bash
```

- Add author to the book with `id=4` using `/books/4` path and HTTP `PUT` method with `curl` command.

```bash
```

- Update book with `id=2` as done using `/books/2` path and HTTP `PUT` method with `curl` command.

```bash
```

- Delete book with `id=1` as done using `/books/1` path and HTTP `PUT` method with `curl` command.

```bash
```

- List all books with latest states from the web browser.

```bash
```
