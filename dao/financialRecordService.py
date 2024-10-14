import pyodbc
from entity.financialRecord import FinancialRecord
from dao.iFinancialRecordService import IFinancialRecordService
from util.dbConnection import DBConnection
from exceptions.financialRecordException import FinancialRecordException
from exceptions.databaseConnectionException import DatabaseConnectionException
from exceptions.invalidInputException import InvalidInputException

class FinancialRecordService(IFinancialRecordService):

    def __init__(self):
        try:
            self.connection = DBConnection.getConnection()
            if self.connection is None:
                raise DatabaseConnectionException("Database connection could not be established.")
        except DatabaseConnectionException as e:
            print(f"Error: {e}")
            raise

    def add_financial_record(self, financial_data):
        try:
            # Validate inputs
            if not all(financial_data):
                raise InvalidInputException("All fields are required for financial record.")
    
            # Insert record into the financialRecord table
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO financialRecord (employeeID, reccordDate, description, amount, recordType) 
                VALUES (?, ?, ?, ?, ?)
            """, financial_data)
            self.connection.commit()
            return True
    
        except InvalidInputException as e:
            print(f"Invalid input: {e}")
            return False
        except Exception as e:
            print(f"Error while adding financial record: {e}")
            return False

    def get_financial_record_by_id(self, record_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from financialRecord where recordID = ?", (record_id,))
            row = cursor.fetchone()

            if row:
                return FinancialRecord(*row)
            else:
                raise FinancialRecordException(f"Financial record with ID {record_id} not found.")
        except FinancialRecordException as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error while fetching financial record: {e}")
            return None

    def get_financial_records_for_employee(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from financialRecord where employeeID = ?", (employee_id,))
            rows = cursor.fetchall()

            records = [FinancialRecord(*row) for row in rows]
            return records
        except Exception as e:
            print(f"Error while fetching financial records: {e}")
            return []

    def get_financial_records_for_date(self, record_date):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from financialRecord where recordDate = ?", (record_date,))
            rows = cursor.fetchall()

            records = [FinancialRecord(*row) for row in rows]
            return records
        except Exception as e:
            print(f"Error while fetching financial records for date {record_date}: {e}")
            return []
