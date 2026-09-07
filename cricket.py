import streamlit as st
from database.connection import test_connection


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Cricket Analytics",
    page_icon="🏏",
    layout="wide"
)


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        text-align: center;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">🏏 Cricket Analytics Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Cricket Data Analysis using API, MySQL & Streamlit'
    '</div>',
    unsafe_allow_html=True
)


# ==========================================
# DATABASE STATUS
# ==========================================

db_status = test_connection()


if db_status:

    st.success("✅ MySQL Database Connected")

else:

    st.error(
        "❌ Database connection failed. "
        "Please check your .env file."
    )


# ==========================================
# KPI CARDS
# ==========================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        "🏏 Platform",
        "Cricket Analytics"
    )


with col2:

    st.metric(
        "🗄️ Database",
        "MySQL"
    )


with col3:

    st.metric(
        "📊 Dashboard",
        "Streamlit"
    )


with col4:

    st.metric(
        "🔌 Data Source",
        "Cricbuzz API"
    )


# ==========================================
# PROJECT OVERVIEW
# ==========================================

st.divider()

st.header("📌 Project Overview")

st.write(
    """
    This application is an end-to-end cricket analytics platform.

    The system collects cricket information through an API,
    stores structured information in MySQL, performs SQL-based
    analytics, and presents results through an interactive
    Streamlit dashboard.
    """
)


# ==========================================
# DATA FLOW
# ==========================================

st.subheader("🔄 Data Flow")

st.info(
    """
    Cricbuzz API
    ↓
    Python API Client
    ↓
    JSON Data
    ↓
    MySQL Database
    ↓
    SQL Analytics
    ↓
    Streamlit Dashboard
    """
)


# ==========================================
# FEATURES
# ==========================================

st.subheader("🚀 Dashboard Features")

col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        ### 🏏 Live Matches

        - View live matches
        - Match status
        - Teams
        - Scores
        - API response
        """
    )

with col2:

    st.markdown(
        """
        ### 🏆 Top Players

        - Top run scorers
        - Batting average
        - Strike rate
        - Player statistics
        """
    )


col1, col2 = st.columns(2)

with col1:

    st.markdown(
        """
        ### 📊 SQL Analytics

        - 25 analytical SQL questions
        - Player analysis
        - Team analysis
        - Match analysis
        - Venue analysis
        """
    )

with col2:

    st.markdown(
        """
        ### ✏️ CRUD

        - Add player
        - Update player
        - Delete player
        - View players
        """
    )


# ==========================================
# FOOTER
# ==========================================

st.divider()

st.caption(
    "Cricket Analytics Project | Python | MySQL | SQL | Streamlit | API"
)