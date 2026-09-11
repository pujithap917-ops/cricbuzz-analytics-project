import streamlit as st
import pandas as pd
import json

from database.connection import CricbuzzClient


st.set_page_config(
    page_title="Live Matches",
    page_icon="🏏",
    layout="wide"
)


st.title("🏏 Live Cricket Matches")

st.write(
    "Fetch live match information from the Cricbuzz API."
)


# ==========================================
# FETCH BUTTON
# ==========================================

if st.button("🔄 Fetch Live Matches"):

    with st.spinner("Fetching live matches..."):

        client = CricbuzzClient()

        data = client.get_live_matches()


    # ======================================
    # ERROR HANDLING
    # ======================================

    if "error" in data:

        st.error(
            f"API Error: {data['error']}"
        )

        if "status_code" in data:

            st.warning(
                f"HTTP Status Code: {data['status_code']}"
            )

        st.info(
            """
            If you receive 404, check the endpoint path
            in your RapidAPI Cricbuzz listing.
            """
        )

    else:

        st.success("✅ API data received successfully!")

        # Store response
        st.session_state["live_data"] = data


# ==========================================
# DISPLAY DATA
# ==========================================

if "live_data" in st.session_state:

    data = st.session_state["live_data"]

    st.subheader("📦 API Response")

    with st.expander("View Raw JSON"):

        st.json(data)


    # ======================================
    # TRY TO CREATE DATAFRAME
    # ======================================

    st.subheader("📊 Match Data")

    if isinstance(data, list):

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True
        )

    elif isinstance(data, dict):

        # Search common list fields

        possible_keys = [
            "matches",
            "data",
            "results",
            "items"
        ]

        found = False

        for key in possible_keys:

            if key in data:

                value = data[key]

                if isinstance(value, list):

                    df = pd.DataFrame(value)

                    st.dataframe(
                        df,
                        use_container_width=True
                    )

                    found = True

                    break


        if not found:

            st.info(
                "The API returned JSON, but its structure "
                "does not contain a recognized match list."
            )

            st.write(data)