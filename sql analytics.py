import streamlit as st
import pandas as pd

from sqlalchemy import text

from database.connection import engine


st.set_page_config(
    page_title="SQL Analytics",
    page_icon="📊",
    layout="wide"
)


st.title("📊 SQL Analytics")

st.write(
    "Run cricket analytics queries using MySQL."
)


# ==========================================
# SQL QUESTIONS
# ==========================================

queries = {

    "Q1 - India Players": """
        SELECT
            player_name,
            role
        FROM players
        WHERE country = 'India'
        ORDER BY player_name;
    """,


    "Q2 - All Players": """
        SELECT
            player_id,
            player_name,
            role,
            country
        FROM players
        ORDER BY player_name;
    """,


    "Q3 - Top 10 Run Scorers": """
        SELECT
            p.player_name,
            SUM(b.runs) AS total_runs
        FROM players p
        JOIN batting_performance b
            ON p.player_id = b.player_id
        GROUP BY
            p.player_id,
            p.player_name
        ORDER BY total_runs DESC
        LIMIT 10;
    """,


    "Q4 - Venues": """
        SELECT
            venue_name,
            city,
            country,
            capacity
        FROM venues
        WHERE capacity > 50000
        ORDER BY capacity DESC;
    """,


    "Q5 - Team Wins": """
        SELECT
            t.team_name,
            COUNT(m.winner_team_id) AS wins
        FROM teams t
        LEFT JOIN matches m
            ON t.team_id = m.winner_team_id
        GROUP BY
            t.team_id,
            t.team_name
        ORDER BY wins DESC;
    """,


    "Q6 - Players By Role": """
        SELECT
            role,
            COUNT(*) AS player_count
        FROM players
        GROUP BY role
        ORDER BY player_count DESC;
    """,


    "Q7 - Highest Batting Score": """
        SELECT
            p.player_name,
            MAX(b.runs) AS highest_score
        FROM players p
        JOIN batting_performance b
            ON p.player_id = b.player_id
        GROUP BY
            p.player_id,
            p.player_name
        ORDER BY highest_score DESC;
    """,


    "Q8 - Series Starting 2024": """
        SELECT
            series_id,
            series_name,
            start_date,
            end_date
        FROM series
        WHERE YEAR(start_date) >= 2024
        ORDER BY start_date;
    """
}


# ==========================================
# SELECT QUERY
# ==========================================

selected_query = st.selectbox(
    "Select SQL Analysis",
    list(queries.keys())
)


# ==========================================
# RUN QUERY
# ==========================================

if st.button("▶ Run Analysis"):

    sql_query = queries[selected_query]

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text(sql_query)
            )

            rows = result.fetchall()

            columns = result.keys()


        if rows:

            df = pd.DataFrame(
                rows,
                columns=columns
            )

            st.success(
                f"✅ {len(df)} rows returned."
            )

            st.dataframe(
                df,
                use_container_width=True
            )


            # ==================================
            # CHART
            # ==================================

            numeric_columns = (
                df.select_dtypes(
                    include="number"
                ).columns
            )


            if len(numeric_columns) > 0:

                st.subheader("📈 Visualization")

                st.bar_chart(
                    df[numeric_columns]
                )


        else:

            st.info(
                "Query executed successfully, "
                "but no records were returned."
            )


    except Exception as e:

        st.error(
            f"SQL Error: {e}"
        )