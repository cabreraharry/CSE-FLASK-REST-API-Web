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


class BooksResource(Resource):
    def get(self, book_id):
    
        pass

    def post(self):
   
        pass

    def put(self, book_id):
    
        pass

    def delete(self, book_id):
  
        pass

class CustomersResource(Resource):

    pass

api.add_resource(BooksResource, '/books/<int:book_id>')
api.add_resource(CustomersResource, '/customers/<int:customer_id>')


if __name__ == '__main__':
    app.run(debug=True)
