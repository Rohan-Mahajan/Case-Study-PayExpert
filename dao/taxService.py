from entity.tax import Tax
from dao.iTaxService import ITaxService
from util.dbConnection import DBConnection
from exceptions.taxCalculationException import TaxCalculationException
from exceptions.databaseConnectionException import DatabaseConnectionException

class TaxService(ITaxService):

    def __init__(self):
        try:
            self.connection = DBConnection.getConnection()
            if self.connection is None:
                raise DatabaseConnectionException("Database connection could not be established.")
        except DatabaseConnectionException as e:
            print(f"Error: {e}")
            raise

    def calculate_tax(self, employee_id, tax_year):
        try:
            # Business logic to calculate tax
            taxable_income = 60000  # Example value
            tax_amount = taxable_income * 0.2  # 20% tax rate
    
            # Print the calculated tax details
            print(f"Employee ID: {employee_id}")
            print(f"Tax Year: {tax_year}")
            print(f"Taxable Income: {taxable_income}")
            print(f"Tax Amount (20%): {tax_amount}")
    
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO tax (employeeID, taxYear, taxableIncome, taxAmount)
                VALUES (?, ?, ?, ?)
            """, (employee_id, tax_year, taxable_income, tax_amount))
            self.connection.commit()
    
            return True
    
        except Exception as e:
            print(f"Error while calculating tax: {e}")
            raise TaxCalculationException("Error in tax calculation")


    def get_tax_by_id(self, tax_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from tax where taxID = ?", (tax_id,))
            row = cursor.fetchone()

            if row:
                return Tax(*row)
            else:
                raise TaxCalculationException(f"Tax record with ID {tax_id} not found.")
        except TaxCalculationException as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error while fetching tax record: {e}")
            return None

    def get_taxes_for_employee(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from tax where employeeID = ?", (employee_id,))
            rows = cursor.fetchall()

            taxes = [Tax(*row) for row in rows]
            return taxes
        except Exception as e:
            print(f"Error while fetching taxes for employee: {e}")
            return []

    def get_taxes_for_year(self, tax_year):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from tax where taxYear = ?", (tax_year,))
            rows = cursor.fetchall()

            taxes = [Tax(*row) for row in rows]
            return taxes
        except Exception as e:
            print(f"Error while fetching taxes for year {tax_year}: {e}")
            return []
        
    