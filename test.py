import unittest
from app import app, mysql

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_get_books(self):
        response = self.app.get("/books")
        self.assertEqual(response.status_code, 200)


    def test_get_books(self):
        with app.app_context():
            response = self.app.get("/books")
            self.assertEqual(response.status_code, 200)
    

    def test_add_book(self):
        book_data = {
            "book_id": 999,  # Use a unique or dynamically generated book_id
            "book_title": "New Book",
            "publication_date": "2022-01-05",
            "book_comments": "Great book!",
        }
        response = self.app.post("/books", json=book_data)
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):

        updated_data = {
            "book_title": "Updated Book Title",
            "publication_date": "2022-02-01",
            "book_comments": "Updated comments"
        }
        response = self.app.put("/books/1", json=updated_data)
        self.assertEqual(response.status_code, 200)
       

    def test_delete_book(self):
        # Add a book first (similar to test_add_book)
        book_data = {
            "book_id": 999,  # Use a unique or dynamically generated book_id
            "book_title": "New Book",
            "publication_date": "2022-01-05",
            "book_comments": "Great book!",
        }
        self.app.post("/books", json=book_data)

        # Now try to delete the book
        response = self.app.delete("/books/999")  # Use the same book_id
        self.assertEqual(response.status_code, 200)

        

if __name__ == "__main__":
    unittest.main()
