import pyodbc

conn_str = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:{servername};Database=pyodbc;Uid={user name};Pwd={password};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

conn = pyodbc.connect(conn_str)