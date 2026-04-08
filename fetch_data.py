import pyodbc
import pandas as pd
import os
import json

# These are read from GitHub Secrets (injected as environment variables)
server   = os.environ["SQL_SERVER"]
database = os.environ["SQL_DATABASE"]
username = os.environ["SQL_USERNAME"]
password = os.environ["SQL_PASSWORD"]

conn_str = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"Encrypt=yes;"
    f"TrustServerCertificate=no;"
)

conn = pyodbc.connect(conn_str)

df = pd.read_sql("SELECT * FROM EDW.fact_ExchangeRate", conn)

conn.close()

# Save to JSON file in the repo
os.makedirs("data", exist_ok=True)
df.to_json("data/currencies.json", orient="records", indent=2)

print(f"Done! {len(df)} rows saved to data/currencies.json")