import os
from dotenv import load_dotenv

load_dotenv()


# ==============================
# DATABASE SETTINGS
# ==============================

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME", "analytics_cricket")
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")


# ==============================
# RAPIDAPI SETTINGS
# ==============================

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "")
RAPIDAPI_HOST = os.getenv(
    "RAPIDAPI_HOST",
    "cricbuzz-api.p.rapidapi.com"
)

API_BASE_URL = f"https://{RAPIDAPI_HOST}"

API_LIVE_PATH = os.getenv(
    "API_LIVE_PATH",
    "/matches/live"
)

API_RECENT_PATH = os.getenv(
    "API_RECENT_PATH",
    "/matches/recent"
)

API_SCHEDULE_PATH = os.getenv(
    "API_SCHEDULE_PATH",
    "/schedule/today"
)