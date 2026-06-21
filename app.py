import streamlit as st
from utils.database import create_database

create_database()

st.set_page_config(
    page_title="AW Financial Portal",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AW Financial Client Portal")

st.write(
    "Quarterly Financial Reporting and Client Management System"
)

st.sidebar.success(
    "AI-Powered Financial Reporting"
)