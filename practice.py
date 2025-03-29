from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

# Load the environment variables

load_dotenv()


# Get credentials from .env file

server = os.getenv("DB_SERVER")
database = os.getenv("DB_NAME")
username = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")

# Create connection string with sqlalchemy

engine = create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server")

try:
    with engine.connect() as conn:
        print("Successfull")
except Exception as e:
    print(f"Error {e}")


def select_all():
    query = "SELECT * FROM Homes"
    df = pd.read_sql(query, engine)
    print(df)


