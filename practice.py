from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

# Load the environment variables

load_dotenv()


# Get credentials from .env file

server = os.env("DB_SERVER")
database = os.env("DB_NAME")
username = os.env("DB_USER")
password = os.env("DB_PASSWORD")

# Create connection string with sqlalchemy

engine = create_engine(f"mssql+pyodbc://{username}")