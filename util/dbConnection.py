import pyodbc
from util.PropertyUtil import PropertyUtil

class DBConnection :
    connection = None

    @staticmethod
    def getConnection() :
        if DBConnection.connection is None :
            try:
                conn_string = PropertyUtil.getConnectionString()
                DBConnection.connection = pyodbc.connect(conn_string)
                print("Connection established successfully.")
            except Exception as e :
                print(f"Connection failed : {e}")
        return DBConnection.connection
