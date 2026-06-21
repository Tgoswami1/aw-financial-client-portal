import streamlit as st

from utils.database import (
    get_clients,
    get_reports
)

st.title("📈 Dashboard")

clients = get_clients()
reports = get_reports()

latest_networth = 0

if reports:
    latest_networth = reports[0][8]

col1, col2, col3 = st.columns(3)

col1.metric(
    "Clients",
    len(clients)
)

col2.metric(
    "Reports Generated",
    len(reports)
)

col3.metric(
    "Latest Net Worth",
    f"${latest_networth:,.0f}"
)

st.divider()

st.subheader("Recent Clients")

if clients:

    for client in clients:

        st.info(
            f"""
Client: {client[1]}

Spouse: {client[2]}
            """
        )

else:

    st.warning("No clients available.")