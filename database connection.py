import mysql.connector

connection = mysql.connector.connect(
 host="localhost",
    port=3306,
    user="root",
   password="YourNewPassword123!",
    database="cricket_analytics"
   )

print("MySQL connected successfully!")


print("Database connected successfully!")

connection.close()
from sqlalchemy import create_engine, text
from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    DB_USER,
    DB_PASSWORD
)


DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)


def get_connection():
    """
    Return a database connection.
    """
    return engine.connect()


def test_connection():
    """
    Test MySQL connection.
    """
    try:
        with engine.connect() as connection:
            result = connection.execute(
                text("SELECT 1")
            )

            return result.fetchone() is not None

    except Exception as e:
        print("Database error:", e)
        return False