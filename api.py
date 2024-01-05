from flask import Flask, make_response, jsonify, request, Response
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "9090"
app.config["MYSQL_DB"] = "customer_at_a_bookstore"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

def data_fetch(query):
    cur = mysql.connection.cursor()
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    return data

@app.route("/")
def home():
    return get_books()


@app.route("/books", methods=["GET"])
def get_books():
    data = data_fetch("SELECT * FROM books")
    return make_response(jsonify(data), 200)

@app.route("/books/<int:book_id>", methods=["GET"])
def get_book_by_id(book_id):
    data = data_fetch(f"SELECT * FROM books WHERE book_id = {book_id}")
    return make_response(jsonify(data), 200)

@app.route("/search/books", methods=["GET"])
def search_books():
    title = request.args.get("title")
    publication_date = request.args.get("publication_date")
    book_comments = request.args.get("book_comments")

    query = "SELECT * FROM books WHERE 1=1"
    if title:
        query += f" AND book_title LIKE '%{title}%'"
    if publication_date:
        query += f" AND publication_date = '{publication_date}'"
    if book_comments:
        query += f" AND book_comments LIKE '%{book_comments}%'"

    data = data_fetch(query)
    return make_response(jsonify(data), 200)


@app.route("/books", methods=["POST"])
def add_book():
    cur = mysql.connection.cursor()
    info = request.get_json()
    book_id = info["book_id"]
    book_title = info["book_title"]
    publication_date = info["publication_date"]
    book_comments = info["book_comments"]
    

    cur.execute(
        """
        INSERT INTO books (book_id, book_title, publication_date, book_comments) 
        VALUES (%s, %s, %s, %s)
        """,
        (book_id, book_title, publication_date, book_comments),
    )
    mysql.connection.commit()
    cur.close()

    return make_response(jsonify({"message": "Book added successfully"}), 201)

@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    cur = mysql.connection.cursor()
    info = request.get_json()
    book_title = info["book_title"]
    publication_date = info["publication_date"]
    book_comments = info["book_comments"]

    cur.execute(
        """
        UPDATE books 
        SET book_title = %s, publication_date = %s, book_comments = %s
        WHERE book_id = %s
        """,
        (book_title, publication_date, book_comments, book_id),
    )
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    return make_response(
        jsonify({"message": "Book updated successfully", "rows_affected": rows_affected}),
        200,
    )

@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM books WHERE book_id = %s", (book_id,))
    mysql.connection.commit()
    rows_affected = cur.rowcount
    cur.close()

    return make_response(
        jsonify({"message": "Book deleted successfully", "rows_affected": rows_affected}),
        200,
    )


# app.config["JWT_SECRET_KEY"] = "your-secret-key"
# jwt = JWTManager(app)

# @app.route("/login", methods=["POST"])
# def login():
#     username = request.json.get("username", None)
#     password = request.json.get("password", None)

#     if username == "harry" and password == "harry123":
#         access_token = create_access_token(identity=username)
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({"message": "Invalid credentials"}), 401


# @app.route("/secure-endpoint", methods=["GET"])
# @jwt_required()
# def secure_endpoint():
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run(debug=True)
