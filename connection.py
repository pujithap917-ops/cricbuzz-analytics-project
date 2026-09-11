import mysql.connector


def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="cricket_db"
    )

    return connection

from database.connection import get_connection

conn = get_connection()

if conn.is_connected():
    print("MySQL connection successful!")

conn.close()