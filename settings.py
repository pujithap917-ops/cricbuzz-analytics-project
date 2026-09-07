import streamlit as st

from config import (
    DB_HOST,
    DB_PORT,
    DB_NAME,
    RAPIDAPI_HOST
)

from database.connection import test_connection


st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)


st.title("⚙️ Settings")


# ==========================================
# DATABASE
# ==========================================

st.subheader("🗄️ Database Configuration")

st.write(
    f"**Host:** {DB_HOST}"
)

st.write(
    f"**Port:** {DB_PORT}"
)

st.write(
    f"**Database:** {DB_NAME}"
)


if test_connection():

    st.success(
        "✅ Database connection is working."
    )

else:

    st.error(
        "❌ Database connection failed."
    )


# ==========================================
# API
# ==========================================

st.divider()

st.subheader("🔌 API Configuration")

st.write(
    f"**RapidAPI Host:** {RAPIDAPI_HOST}"
)

st.info(
    """
    Your API key is intentionally not displayed.
    Never expose your RapidAPI key in GitHub,
    screenshots or public code.
    """
)