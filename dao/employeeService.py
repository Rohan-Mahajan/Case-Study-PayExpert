import pyodbc
from entity.employee import Employee
from dao.iEmployeeService import IEmployeeService
from util.dbConnection import DBConnection  # Assuming you have DBConnection set up
from exceptions.employeeNotFoundException import EmployeeNotFoundException
from exceptions.databaseConnectionException import DatabaseConnectionException
from exceptions.invalidInputException import InvalidInputException

class EmployeeService(IEmployeeService):

    def __init__(self):
        # Attempt to establish a database connection
        try:
            self.connection = DBConnection.getConnection()  # Assuming DBConnection provides a valid connection
            if self.connection is None:
                raise DatabaseConnectionException("Database connection could not be established.")
        except DatabaseConnectionException as e:
            print(f"Error: {e}")
            raise

    def get_employee_by_id(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from employee where employeeID = ?", (employee_id,))
            row = cursor.fetchone()

            if row:
                return Employee(*row)
            else:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
        except EmployeeNotFoundException as e:
            print(f"Error: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error while fetching employee: {e}")
            return None

    def get_all_employees(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select * from employee")
            rows = cursor.fetchall()

            employees = [Employee(*row) for row in rows]
            return employees
        except Exception as e:
            print(f"Error while fetching all employees: {e}")
            return []

    def add_employee(self, employee_data):
        try:
            if not all(employee_data):  # Basic validation check
                raise InvalidInputException("All employee data fields must be provided.")

            cursor = self.connection.cursor()
            cursor.execute("""
                insert into employee (employeeId, firstName, lastName, dateOfBirth, gender, email, phoneNumber, address, position, joiningDate)
                value (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, employee_data)
            self.connection.commit()
            return True
        except InvalidInputException as e:
            print(f"Invalid input: {e}")
            return False
        except Exception as e:
            print(f"Error while adding employee: {e}")
            return False

    def update_employee(self, employee_data):
        try:
            if not employee_data[-1]:  # Assuming last field is EmployeeID
                raise InvalidInputException("EmployeeID is required for updating an employee.")

            cursor = self.connection.cursor()
            cursor.execute("""
                update employee set firstName = ?, lastName = ?, dateOfBirth = ?, gender = ?, email = ?, phoneNumber = ?, address = ?, position = ?, joiningDate = ?
                where employeeID = ?
            """, employee_data)
            self.connection.commit()
            return True
        except InvalidInputException as e:
            print(f"Invalid input: {e}")
            return False
        except Exception as e:
            print(f"Error while updating employee: {e}")
            return False

    def remove_employee(self, employee_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("delete from employee where employeeID = ?", (employee_id,))
            if cursor.rowcount == 0:
                raise EmployeeNotFoundException(f"Employee with ID {employee_id} not found.")
            self.connection.commit()
            return True
        except EmployeeNotFoundException as e:
            print(f"Error: {e}")
            return False
        except Exception as e:
            print(f"Error while removing employee: {e}")
            return False
