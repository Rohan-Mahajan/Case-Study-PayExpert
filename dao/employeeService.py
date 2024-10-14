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
                insert into employee (firstName, lastName, dateOfBirth, gender, email, phoneNumber, address, position, joiningDate)
                values (?, ?, ?, ?, ?, ?, ?, ?, ?)
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
            if not employee_data.get('employee_id'):
                raise InvalidInputException("EmployeeID is required for updating an employee.")
    
            set_clause = []
            parameters = []
    
            # Build SET clause dynamically based on provided data
            if employee_data['first_name']:
                set_clause.append("firstName = ?")
                parameters.append(employee_data['first_name'])
            if employee_data['last_name']:
                set_clause.append("lastName = ?")
                parameters.append(employee_data['last_name'])
            if employee_data['dob']:
                set_clause.append("dateOfBirth = ?")
                parameters.append(employee_data['dob'])
            if employee_data['gender']:
                set_clause.append("gender = ?")
                parameters.append(employee_data['gender'])
            if employee_data['email']:
                set_clause.append("email = ?")
                parameters.append(employee_data['email'])
            if employee_data['phone']:
                set_clause.append("phoneNumber = ?")
                parameters.append(employee_data['phone'])
            if employee_data['address']:
                set_clause.append("address = ?")
                parameters.append(employee_data['address'])
            if employee_data['position']:
                set_clause.append("position = ?")
                parameters.append(employee_data['position'])
            if employee_data['joining_date']:
                set_clause.append("joiningDate = ?")
                parameters.append(employee_data['joining_date'])
    
            # Add the employee ID to the end of parameters list
            parameters.append(employee_data['employee_id'])
    
            cursor = self.connection.cursor()
            cursor.execute(f"""
                UPDATE employee 
                SET {', '.join(set_clause)} 
                WHERE employeeID = ?
            """, parameters)
            
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
