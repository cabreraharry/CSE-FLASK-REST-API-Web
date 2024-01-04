from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "9090"
app.config["MYSQL_DB"] = "customer_at_a_bookstore"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["SECRET_KEY"] = "817b92cd83a065429e25a11dbddc0ebf"

mysql = MySQL(app)


if __name__ == "__main__":
    app.run(debug=True)
