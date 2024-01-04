import unittest
import json
from unittest.mock import patch
from app import app

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    @patch('app.data_fetch')
    def test_get_books(self, mock_data_fetch):
        mock_data_fetch.return_value = [{"book_id": 1, "book_title": "Test Book"}]
        response = self.app.get("/books")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data, [{"book_id": 1, "book_title": "Test Book"}])

    @patch('app.data_fetch')
    def test_get_book_by_id(self, mock_data_fetch):
        mock_data_fetch.return_value = [{"book_id": 1, "book_title": "Test Book"}]
        response = self.app.get("/books/1")
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data.decode())
        self.assertEqual(data, [{"book_id": 1, "book_title": "Test Book"}])

    def test_add_book(self):
        with patch('app.request.get_json', return_value={
            "book_id": 1,
            "book_title": "Test Book",
            "publication_date": "2022-01-01",
            "book_comments": "Test Comments",
        }):
            response = self.app.post("/books")
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):
        with patch('app.request.get_json', return_value={
            "book_title": "Updated Book",
            "publication_date": "2023-01-01",
            "book_comments": "Updated Comments",
        }):
            response = self.app.put("/books/1")
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):
        response = self.app.delete("/books/1")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
