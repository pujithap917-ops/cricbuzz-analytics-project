import os

from dotenv import load_dotenv


load_dotenv()


DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv(
    "DB_NAME",
    "analytics_cricket"
)
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


RAPIDAPI_KEY = os.getenv(
    "RAPIDAPI_KEY",
    ""
)

RAPIDAPI_HOST = os.getenv(
    "RAPIDAPI_HOST",
    ""
)