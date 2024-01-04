from flask import Flask
from flask_restful import Resource, Api, reqparse
import mysql.connector

app = Flask(__name__)
api = Api(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="9090",
    database="customer_at_a_bookstore"
)
cursor = db.cursor(dictionary=True)

parser = reqparse.RequestParser()
parser.add_argument('book_title')
parser.add_argument('publication_date')
parser.add_argument('book_comments')

class BooksResource(Resource):
    def get(self, book_id):
        cursor.execute(f"SELECT * FROM books WHERE book_id = {book_id}")
        book = cursor.fetchone()
        if book:
            return book, 200
        else:
            return {"message": "Book not found"}, 404

    def post(self):
        args = parser.parse_args()
        cursor.execute(f"INSERT INTO books (book_title, publication_date, book_comments) VALUES ('{args['book_title']}', '{args['publication_date']}', '{args['book_comments']}')")
        db.commit()
        return {"message": "Book added successfully"}, 201

    def put(self, book_id):
        args = parser.parse_args()
        cursor.execute(f"UPDATE books SET book_title = '{args['book_title']}', publication_date = '{args['publication_date']}', book_comments = '{args['book_comments']}' WHERE book_id = {book_id}")
        db.commit()
        return {"message": "Book updated successfully"}, 200

    def delete(self, book_id):
        cursor.execute(f"DELETE FROM books WHERE book_id = {book_id}")
        db.commit()
        return {"message": "Book deleted successfully"}, 200

class CustomersResource(Resource):
    def get(self, customer_id):
        cursor.execute(f"SELECT * FROM customers WHERE customer_id = {customer_id}")
        customer = cursor.fetchone()
        if customer:
            return customer, 200
        else:
            return {"message": "Customer not found"}, 404

api.add_resource(BooksResource, '/books/<int:book_id>')
api.add_resource(CustomersResource, '/customers/<int:customer_id>')

if __name__ == '__main__':
    app.run(debug=True)
