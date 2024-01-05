import unittest
from flask import json
from api import app

class MyApiTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json.loads(response.data), list))

    def test_get_book_by_id(self):
        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json.loads(response.data), list))

    def test_search_books(self):
        response = self.app.get('/search/books?title=Title&publication_date=2022-01-01&book_comments=Comment')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(isinstance(json.loads(response.data), list))

    def test_add_book(self):
        data = {
            'book_id': 100,
            'book_title': 'Test Book',
            'publication_date': '2022-01-01',
            'book_comments': 'Test Comment'
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
