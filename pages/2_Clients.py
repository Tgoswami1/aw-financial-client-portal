import streamlit as st

from utils.database import (
    insert_client,
    get_clients
)

st.title("👥 Client Management")

st.subheader("Add Client")

client_name = st.text_input(
    "Client Name"
)

spouse_name = st.text_input(
    "Spouse Name"
)

salary = st.number_input(
    "Annual Salary",
    min_value=0.0
)

expenses = st.number_input(
    "Monthly Expenses",
    min_value=0.0
)

deductibles = st.number_input(
    "Insurance Deductibles",
    min_value=0.0
)

if st.button("Save Client"):

    insert_client(
        client_name,
        spouse_name,
        salary,
        expenses,
        deductibles
    )

    st.success("Client saved successfully.")

st.divider()

st.subheader("Client List")

clients = get_clients()

if clients:

    for client in clients:

        st.info(
            f"""
Client: {client[1]}

Spouse: {client[2]}

Salary: ${client[3]:,.0f}

Monthly Expenses: ${client[4]:,.0f}
            """
        )

else:

    st.warning("No clients found.")