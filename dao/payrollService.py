import pyodbc
from entity.payroll import Payroll
from dao.iPayrollService import IPayrollService
from util.dbConnection import DBConnection
from exceptions.payrollGenerateException import PayrollGenerationException
from exceptions.databaseConnectionException import DatabaseConnectionException

class PayrollService(IPayrollService):

    def __init__(self):
        try:
            self.connection = DBConnection.getConnection()
            if self.connection is None:
                raise DatabaseConnectionException("Database connection could not be established.")
        except DatabaseConnectionException as e:
            print(f"Error: {e}")
            raise

    def generate_payroll(self, payroll_data):
        try:
            # Business logic can be expanded here
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO payroll (employeeID, payPeriodStartDate, payPeriodEndDate, basicSalary, overTimePay, deductions)
                VALUES (?, ?, ?, ?, ?, ?)
            """, payroll_data)  
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Error while generating payroll: {e}")
            raise PayrollGenerationException("Failed to generate payroll")

    def get_payroll_by_id(self, payroll_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from payroll where payrollID = ?", (payroll_id,))
            row = cursor.fetchone()

            if row:
                return Payroll(*row)
            else:
                raise PayrollGenerationException(f"Payroll with ID {payroll_id} not found.")
        except PayrollGenerationException as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error while fetching payroll: {e}")
            return None

    def get_payrolls_for_employee(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from payroll where employeeID = ?", (employee_id,))
            rows = cursor.fetchall()

            payrolls = [Payroll(*row) for row in rows]
            return payrolls
        except Exception as e:
            print(f"Error while fetching payrolls for employee: {e}")
            return []

    def get_payrolls_for_period(self, start_date, end_date):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                select * from payroll 
                where payPeriodStartDate >= ? and payPeriodEndDate <= ?
            """, (start_date, end_date))
            rows = cursor.fetchall()

            payrolls = [Payroll(*row) for row in rows]
            return payrolls
        except Exception as e:
            print(f"Error while fetching payrolls for period: {e}")
            return []
        
    # Method to calculate net salary
    def calculate_net_salary(self, basic_salary, overtime_pay, deductions):
        return basic_salary + overtime_pay - deductions

    # Method to calculate gross salary
    def calculate_gross_salary(self, basic_salary, overtime_pay):
        return basic_salary + overtime_pay
