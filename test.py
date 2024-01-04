import unittest
import warnings
from app import app, mysql

class MyAppTests(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        app.config["MYSQL_DB"] = "test_customer_at_a_bookstore"  
        self.app = app.test_client()

        warnings.simplefilter("ignore", category=DeprecationWarning)


        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute("CREATE DATABASE IF NOT EXISTS test_customer_at_a_bookstore")
            cur.execute("USE test_customer_at_a_bookstore")
            cur.execute("DROP TABLE IF EXISTS books")
            cur.execute("""
                CREATE TABLE books (
                    book_id int PRIMARY KEY,
                    book_title varchar(255),
                    publication_date datetime,
                    book_comments varchar(255)
                )
            """)

            mysql.connection.commit()
            cur.close()

    def tearDown(self):

        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute("DROP DATABASE IF EXISTS test_customer_at_a_bookstore")
            mysql.connection.commit()
            cur.close()

    def test_get_books(self):
        response = self.app.get("/books")
        self.assertEqual(response.status_code, 200)

    def test_add_book(self):
        response = self.app.post(
            "/books",
            json={
                "book_id": 1,
                "book_title": "Test Book",
                "publication_date": "2022-01-01",
                "book_comments": "Test Comments",
            },
        )
        self.assertEqual(response.status_code, 201)

    def test_update_book(self):

        self.app.post(
            "/books",
            json={
                "book_id": 1,
                "book_title": "Test Book",
                "publication_date": "2022-01-01",
                "book_comments": "Test Comments",
            },
        )
        response = self.app.put(
            "/books/1",
            json={
                "book_title": "Updated Book",
                "publication_date": "2023-01-01",
                "book_comments": "Updated Comments",
            },
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_book(self):

        self.app.post(
            "/books",
            json={
                "book_id": 1,
                "book_title": "Test Book",
                "publication_date": "2022-01-01",
                "book_comments": "Test Comments",
            },
        )
        response = self.app.delete("/books/1")
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
