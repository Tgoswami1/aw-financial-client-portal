import streamlit as st
from datetime import date
import pandas as pd

from utils.database import (
    get_clients,
    insert_report,
    get_reports
)

from utils.calculations import (
    calculate_target,
    calculate_net_worth
)

from utils.pdf_generator import generate_pdf

st.title("📄 Quarterly Reports")

clients = get_clients()

if not clients:

    st.warning(
        "Please add a client first."
    )

else:

    client_names = [
        client[1]
        for client in clients
    ]

    selected_name = st.selectbox(
        "Select Client",
        client_names
    )

    selected_client = None

    for client in clients:

        if client[1] == selected_name:
            selected_client = client

    st.divider()

    st.subheader("Client Summary")

    col1, col2 = st.columns(2)

    col1.write(
        f"Client: {selected_client[1]}"
    )

    col1.write(
        f"Spouse: {selected_client[2]}"
    )

    col2.write(
        f"Salary: ${selected_client[3]:,.0f}"
    )

    col2.write(
        f"Monthly Expenses: ${selected_client[4]:,.0f}"
    )

    st.divider()

    st.subheader(
        "Quarterly Financial Data"
    )

    private_reserve = st.number_input(
        "Private Reserve",
        min_value=0.0
    )

    investment_balance = st.number_input(
        "Investment Balance",
        min_value=0.0
    )

    trust_value = st.number_input(
        "Trust Value",
        min_value=0.0
    )

    liabilities = st.number_input(
        "Liabilities",
        min_value=0.0
    )

    st.divider()

    st.subheader("Validation")

    if private_reserve == 0:
        st.warning(
            "Private Reserve missing."
        )

    if investment_balance == 0:
        st.warning(
            "Investment Balance missing."
        )

    if trust_value == 0:
        st.warning(
            "Trust Value missing."
        )

    target = calculate_target(
        selected_client[4],
        selected_client[5]
    )

    net_worth = calculate_net_worth(
        private_reserve,
        investment_balance,
        trust_value
    )

    st.divider()

    col1, col2 = st.columns(2)

    col1.metric(
        "Savings Target",
        f"${target:,.0f}"
    )

    col2.metric(
        "Net Worth",
        f"${net_worth:,.0f}"
    )

    if st.button("Save Report"):

        report_date = str(date.today())

        insert_report(
            selected_client[0],
            report_date,
            private_reserve,
            investment_balance,
            trust_value,
            liabilities,
            target,
            net_worth
        )

        st.success(
            "Report saved successfully."
        )

        pdf_file = generate_pdf(
            selected_client[1],
            report_date,
            target,
            net_worth,
            private_reserve,
            investment_balance,
            trust_value,
            liabilities
        )

        with open(pdf_file, "rb") as file:

            st.download_button(
                "📥 Download PDF",
                file,
                file_name=pdf_file,
                mime="application/pdf"
            )

    st.divider()

    st.subheader("Report History")

    reports = get_reports()

    if reports:

        df = pd.DataFrame(
            reports,
            columns=[
                "ID",
                "Client ID",
                "Date",
                "Reserve",
                "Investment",
                "Trust",
                "Liabilities",
                "Savings",
                "Net Worth"
            ]
        )

        st.dataframe(
            df,
            use_container_width=True
        )