import streamlit as st
import pandas as pd
from sqlalchemy import text

from database.connection import engine


st.set_page_config(
    page_title="Top Players",
    page_icon="🏆",
    layout="wide"
)


st.title("🏆 Top Players")

st.write(
    "Analyze player batting and bowling performance."
)


# ==========================================
# LOAD PLAYERS
# ==========================================

try:

    query = """
        SELECT
            p.player_id,
            p.player_name,
            p.role
        FROM players p
        ORDER BY p.player_name
    """

    with engine.connect() as connection:

        result = connection.execute(
            text(query)
        )

        rows = result.fetchall()


    if rows:

        df = pd.DataFrame(
            rows,
            columns=result.keys()
        )

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No player data available."
        )


except Exception as e:

    st.error(
        f"Database error: {e}"
    )


# ==========================================
# TOP RUN SCORERS
# ==========================================

st.divider()

st.subheader("🏏 Top Run Scorers")


try:

    query = """
        SELECT
            p.player_name,
            SUM(b.runs) AS total_runs,
            COUNT(b.performance_id) AS innings
        FROM players p
        JOIN batting_performance b
            ON p.player_id = b.player_id
        GROUP BY
            p.player_id,
            p.player_name
        ORDER BY total_runs DESC
        LIMIT 10
    """

    with engine.connect() as connection:

        result = connection.execute(
            text(query)
        )

        rows = result.fetchall()


    if rows:

        df = pd.DataFrame(
            rows,
            columns=result.keys()
        )

        st.dataframe(
            df,
            use_container_width=True
        )

        st.bar_chart(
            df.set_index("player_name")["total_runs"]
        )

    else:

        st.info(
            "No batting performance data available."
        )


except Exception as e:

    st.error(
        f"Unable to calculate top scorers: {e}"
    )