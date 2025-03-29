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


def connect_and_export():

    #Connects to the databse, retrieves data then saves it to an Excel file

    try:
        with engine.connect() as conn:
            
            query = "SELECT * FROM Homes"

            df = pd.read_sql(query, conn)

            excel_file = "homes_info.xlsx"

            df.to_excel(excel_file, index=False)

            print(f"The data has been written to {excel_file}")
    except Exception as e:
        print("Error occured, {e}")


connect_and_export()



# try:
#     with engine.connect() as conn:
#         print("Successfull")

        
# except Exception as e:
#     print(f"Error {e}")


# def select_all():
#     query = "SELECT * FROM Homes"
#     df = pd.read_sql(query, engine)
#     print(df)


