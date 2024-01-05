import unittest
from flask import json
from api import app, mysql

class MyApiTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.app.testing = True

        # Create a test book for the database
        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute(
                """
                INSERT INTO books (book_id, book_title, publication_date, book_comments) 
                VALUES (1, 'Test Book', '2022-01-01', 'Test Comment')
                """
            )
            mysql.connection.commit()
            cur.close()

    def tearDown(self):
        # Clean up the test data after each test
        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute("DELETE FROM books WHERE book_id = 1")
            mysql.connection.commit()
            cur.close()

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(len(data), 21)  # Expecting only one book in the response

    def test_get_book_by_id(self):
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)  # Expecting only one book in the response

    def test_search_books(self):
        response = self.app.get('/search/books?title=Test&publication_date=2022-01-01&book_comments=Test')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(isinstance(data, list))
        self.assertEqual(len(data), 1)  # Expecting only one book in the response

    def test_add_book(self):
        data = {
            'book_id': 100,  # Change the book_id to avoid duplicates
            'book_title': 'New Book',
            'publication_date': '2022-01-02',
            'book_comments': 'New Comment'
        }
        response = self.app.post('/books', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(json.loads(response.data), {'message': 'Book added successfully'})

    def test_update_book(self):
        data = {
            'book_title': 'Updated Book',
            'publication_date': '2023-01-01',
            'book_comments': 'Updated Comment'
        }
        response = self.app.put('/books/1', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Book updated successfully', 'rows_affected': 1})

    def test_delete_book(self):
        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.data), {'message': 'Book deleted successfully', 'rows_affected': 1})

if __name__ == '__main__':
    unittest.main()
