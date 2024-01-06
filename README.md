API Overview
The API is a basic implementation for managing books in a bookstore. It provides endpoints for retrieving all books, getting a book by its ID, searching for books based on various criteria, adding a new book, updating an existing book, and deleting a book.

Endpoints
1. Home
URL: /
Method: GET
Description: Returns the list of all books.
Response:
Status Code: 200 OK
Body: A JSON array containing book information.
2. Get Books
URL: /books
Method: GET
Description: Returns the list of all books.
Response:
Status Code: 200 OK
Body: A JSON array containing book information.
3. Get Book by ID
URL: /books/<int:book_id>
Method: GET
Description: Returns information about a specific book based on its ID.
Response:
Status Code: 200 OK
Body: A JSON array containing book information.
4. Search Books
URL: /search/books
Method: GET
Description: Searches for books based on specified criteria (title, publication date, and book comments).
Query Parameters:
title (optional): Title of the book to search for.
publication_date (optional): Publication date of the book to search for.
book_comments (optional): Comments associated with the book to search for.
Response:
Status Code: 200 OK
Body: A JSON array containing book information.
5. Add Book
URL: /books
Method: POST
Description: Adds a new book to the database.
Request Body:
JSON object with the following fields:
book_id (int): Unique identifier for the book.
book_title (string): Title of the book.
publication_date (string): Publication date of the book (format: 'YYYY-MM-DD').
book_comments (string): Comments associated with the book.
Response:
Status Code: 201 Created
Body: A JSON object with a success message.
6. Update Book
URL: /books/<int:book_id>
Method: PUT
Description: Updates the information of an existing book based on its ID.
Request Body:
JSON object with the following fields (at least one field is required):
book_title (string): New title of the book.
publication_date (string): New publication date of the book (format: 'YYYY-MM-DD').
book_comments (string): New comments associated with the book.
Response:
Status Code: 200 OK
Body: A JSON object with a success message and the number of rows affected.
7. Delete Book
URL: /books/<int:book_id>
Method: DELETE
Description: Deletes a book from the database based on its ID.
Response:
Status Code: 200 OK
Body: A JSON object with a success message and the number of rows affected.
Testing
The testing is implemented using the unittest framework. The tests.py file contains test cases for each endpoint to ensure the functionality of the API. To run the tests, execute the following command:


python tests.py

The tests include:

test_get_books: Checks if the endpoint for retrieving all books returns the expected response.
test_get_book_by_id: Checks if the endpoint for retrieving a book by ID returns the expected response.
test_search_books: Checks if the endpoint for searching books returns the expected response.
test_add_book: Checks if the endpoint for adding a new book returns the expected response.
test_update_book: Checks if the endpoint for updating a book returns the expected response.
test_delete_book: Checks if the endpoint for deleting a book returns the expected response.