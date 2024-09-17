import pandas as pd
import pyodbc as odbc
print(odbc.drivers())

DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'DESKTOP-3HMBNTJ\SQLEXPRESS'
DATABASE_NAME = 'aiagent'
connection = f"""
DRIVER = {{{DRIVER_NAME}}};
                    SERVER = {SERVER_NAME};
                    DATABASE = {DATABASE_NAME};
                    Trust_Connection=yes;
                    UID = dbo;
                    PWD = DESKTOP-3HMBNTJ;
"""
conn = odbc.connect(connection)

'''df = pd.read_csv("sql_ai_agent/database_clients.csv")
print(df)'''