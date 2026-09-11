import streamlit as st
import pandas as pd
from sqlalchemy import text
from database.connection import engine

# Inside pages/crud.py
from database.connection import get_connection

# Call the function to get the engine
engine = get_connection()

st.set_page_config(
    page_title="CRUD",
    page_icon="✏️",
    layout="wide"
)

st.title("✏️ Player CRUD Operations")

# ==========================================
# VIEW PLAYERS
# ==========================================
st.subheader("👥 View Players")

def load_players():
    query = """
        SELECT
            player_id,
            player_name,
            role,
            country
        FROM players
        ORDER BY player_name
    """
    # Using pd.read_sql is cleaner and faster than fetching rows manually
    with engine.connect() as connection:
        return pd.read_sql(text(query), connection)

try:
    df = load_players()
    st.dataframe(df, use_container_width=True)
except Exception as e:
    st.error(f"Error loading players: {e}")

st.divider()

# ==========================================
# ADD PLAYER
# ==========================================
st.subheader("➕ Add Player")

with st.form("add_player_form"):
    player_name = st.text_input("Player Name")
    role = st.selectbox(
        "Role",
        ["Batsman", "Bowler", "All-rounder", "Wicketkeeper"]
    )
    country = st.text_input("Country")
    submit = st.form_submit_button("Add Player")

if submit:
    if not player_name.strip():
        st.warning("Player name is required.")
    else:
        try:
            query = """
                INSERT INTO players (player_name, role, country)
                VALUES (:player_name, :role, :country)
            """
            with engine.begin() as connection:
                connection.execute(
                    text(query),
                    {
                        "player_name": player_name.strip(),
                        "role": role,
                        "country": country.strip()
                    }
                )
            
            st.success("✅ Player added successfully!")
            st.rerun()

        except Exception as e:
            st.error(f"Insert error: {e}")

# ==========================================
# DELETE PLAYER
# ==========================================
st.divider()
st.subheader("🗑️ Delete Player")

# Added value=1 to ensure the return type is an integer, not a float
player_id = st.number_input("Player ID", min_value=1, step=1, value=1)

if st.button("Delete Player"):
    try:
        query = """
            DELETE FROM players
            WHERE player_id = :player_id
        """
        with engine.begin() as connection:
            result = connection.execute(
                text(query),
                {"player_id": player_id}
            )

        if result.rowcount > 0:
            st.success("✅ Player deleted successfully!")
            st.rerun()
        else:
            st.warning("Player ID not found.")

    except Exception as e:
        st.error(f"Delete error: {e}")