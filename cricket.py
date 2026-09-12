import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Cricbuzz Cricket Dashboard",
    page_icon="🏏",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        margin-bottom: 30px;
    }

    .card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        text-align: center;
    }

    .card h2 {
        margin: 0;
        font-size: 30px;
    }

    .card p {
        margin: 5px 0 0 0;
        font-size: 16px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🏏 Cricbuzz Cricket Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Live cricket information, player analytics and SQL insights'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

st.sidebar.title("🏏 Cricket Analytics")

st.sidebar.write(
    "Use the pages below to explore cricket data."
)

st.sidebar.divider()

st.sidebar.info(
    """
    **Project Modules**

    🔴 Live Matches  
    🏆 Top Players  
    📊 SQL Analytics  
    ✏️ CRUD Operations  
    ⚙️ Settings
    """
)

# ---------------------------------------------------------
# API STATUS
# ---------------------------------------------------------

rapidapi_key = os.getenv("RAPIDAPI_KEY")
rapidapi_host = os.getenv("RAPIDAPI_HOST")

# ---------------------------------------------------------
# KPI CARDS
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🏏 Project",
        value="Cricbuzz"
    )

with col2:
    st.metric(
        label="📊 Analytics",
        value="25 SQL"
    )

with col3:
    st.metric(
        label="🗄️ Database",
        value="MySQL"
    )

with col4:
    st.metric(
        label="📈 Dashboard",
        value="Streamlit"
    )

st.divider()

# ---------------------------------------------------------
# PROJECT OVERVIEW
# ---------------------------------------------------------

st.subheader("📌 Project Overview")

st.write(
    """
    This project is an end-to-end cricket analytics application.

    Cricket data is collected through the Cricbuzz API,
    stored and managed using MySQL, analyzed using SQL/Python,
    and presented through an interactive Streamlit dashboard.
    """
)

# ---------------------------------------------------------
# ARCHITECTURE
# ---------------------------------------------------------

st.subheader("🔄 Data Flow")

flow1, flow2, flow3, flow4, flow5 = st.columns(5)

with flow1:
    st.info("🌐\n\n**Cricbuzz API**")

with flow2:
    st.info("🐍\n\n**Python**")

with flow3:
    st.info("🗄️\n\n**MySQL**")

with flow4:
    st.info("📊\n\n**SQL Analytics**")

with flow5:
    st.info("💻\n\n**Streamlit**")

# ---------------------------------------------------------
# API CONNECTION STATUS
# ---------------------------------------------------------

st.divider()

st.subheader("🔌 API Configuration")

if rapidapi_key and rapidapi_host:

    st.success("✅ RapidAPI configuration found.")

    st.write(
        f"**API Host:** `{rapidapi_host}`"
    )

else:

    st.warning(
        "⚠️ RapidAPI credentials are not configured."
    )

    st.write(
        """
        Add the following variables to your `.env` file:

        `RAPIDAPI_KEY=your_api_key`

        `RAPIDAPI_HOST=your_api_host`
        """
    )

# ---------------------------------------------------------
# DATABASE STATUS
# ---------------------------------------------------------

st.subheader("🗄️ Database")

db_name = os.getenv(
    "DB_NAME",
    "analytics_cricket"
)

db_host = os.getenv(
    "DB_HOST",
    "localhost"
)

st.write(
    f"**Database:** `{db_name}`"
)

st.write(
    f"**Host:** `{db_host}`"
)

# ---------------------------------------------------------
# PROJECT FEATURES
# ---------------------------------------------------------

st.divider()

st.subheader("✨ Dashboard Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.markdown(
        """
        ### 🏏 Cricket Data

        - Live matches
        - Recent matches
        - Upcoming matches
        - Teams
        - Players
        - Series
        - Venues
        """
    )

with feature2:

    st.markdown(
        """
        ### 📊 Analytics

        - Top run scorers
        - Top wicket takers
        - Player performance
        - Team wins
        - Venue analysis
        - Format comparison
        - SQL analytics
        """
    )

# ---------------------------------------------------------
# QUICK START
# ---------------------------------------------------------

st.divider()

st.subheader("🚀 Quick Start")

st.write(
    """
    Use the **pages menu in the sidebar** to open the different
    modules of the cricket analytics application.
    """
)

st.markdown(
    """
    **Recommended order:**

    1. 🔴 Live Matches
    2. 🏆 Top Players
    3. 📊 SQL Analytics
    4. ✏️ CRUD
    5. ⚙️ Settings
    """
)

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.divider()

st.caption(
    "Cricbuzz Cricket Analytics Project | Python + MySQL + SQL + Streamlit"
)