from flask import Flask
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

app.secret_key = 'rbvgjkihhofesdeplvzrqrtlefnlquze'
# database connection details
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'ECOLION'
# Intialize MySQL
mysql = MySQL(app)

# Executes input function on a cursor called on the query input, and returns the result of the function
def execute(query, args=(), cursor_access=lambda cursor: None):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  # type:ignore
    if type(args) is not tuple:
        args = (args,)
    cursor.execute(query, args)
    return_value = cursor_access(cursor)
    cursor.close()
    return return_value

def dbfetch(query, args=(), one=False):
    def fetch_data(cursor):
        if one:
            return cursor.fetchone()
        return cursor.fetchall()

    return execute(query, args, cursor_access=fetch_data)

def dbcommit(query, args=()):
    result = execute(query, args)
    try:
        mysql.connection.commit()  # type:ignore
    except Exception as e:
        print("MySQL Error", e)
    return result
