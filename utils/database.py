import sqlite3
import os

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DB_PATH = os.path.join(
    BASE_DIR,
    "database",
    "app.db"
)


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_database():

    os.makedirs(
        os.path.dirname(DB_PATH),
        exist_ok=True
    )

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_name TEXT,
            spouse_name TEXT,
            salary REAL,
            expense_budget REAL,
            insurance_deductibles REAL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER,
            report_date TEXT,
            private_reserve REAL,
            investment_balance REAL,
            trust_value REAL,
            liabilities REAL,
            savings_target REAL,
            net_worth REAL
        )
    """)

    conn.commit()
    conn.close()


def insert_client(
    client_name,
    spouse_name,
    salary,
    expense_budget,
    insurance_deductibles
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clients
        (
            client_name,
            spouse_name,
            salary,
            expense_budget,
            insurance_deductibles
        )
        VALUES (?, ?, ?, ?, ?)
    """,
    (
        client_name,
        spouse_name,
        salary,
        expense_budget,
        insurance_deductibles
    ))

    conn.commit()
    conn.close()


def get_clients():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM clients"
    )

    data = cursor.fetchall()

    conn.close()

    return data


def insert_report(
    client_id,
    report_date,
    private_reserve,
    investment_balance,
    trust_value,
    liabilities,
    savings_target,
    net_worth
):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO reports
        (
            client_id,
            report_date,
            private_reserve,
            investment_balance,
            trust_value,
            liabilities,
            savings_target,
            net_worth
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        client_id,
        report_date,
        private_reserve,
        investment_balance,
        trust_value,
        liabilities,
        savings_target,
        net_worth
    ))

    conn.commit()
    conn.close()


def get_reports():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM reports
        ORDER BY id DESC
    """)

    reports = cursor.fetchall()

    conn.close()

    return reports