from entity.payroll import Payroll
from dao.employeeService import EmployeeService
from dao.payrollService import PayrollService
from dao.taxService import TaxService
from dao.financialRecordService import FinancialRecordService
from exceptions.employeeNotFoundException import EmployeeNotFoundException
from exceptions.payrollGenerateException import PayrollGenerationException
from exceptions.taxCalculationException import TaxCalculationException
from exceptions.financialRecordException import FinancialRecordException
from exceptions.invalidInputException import InvalidInputException
from exceptions.databaseConnectionException import DatabaseConnectionException

class PayrollManagementSystem:
    """Main class for handling the Payroll Management System operations."""

    def __init__(self):
        # Initialize service instances (they handle their own database connections)
        try:
            self.employee_service = EmployeeService()  # Create an instance of EmployeeService
            self.payroll_service = PayrollService()    # Create an instance of PayrollService
            self.tax_service = TaxService()            # Create an instance of TaxService
            self.financial_service = FinancialRecordService()  # Create an instance of FinancialRecordService
            print("Service instances initialized successfully.")
        except DatabaseConnectionException as e:
            print(f"Error: {str(e)}")
            raise

    def display_menu(self):
        # Display the main menu and handle user input for different operations
        while True:
            print("\n===== Payroll Management System Menu =====")
            print("1. Add a new Employee")
            print("2. Get Employee by ID")
            print("3. Get All Employees")
            print("4. Update Employee")
            print("5. Remove Employee")
            print("6. Get Payroll by ID")
            print("7. Add Payroll")
            print("8. Get Payrolls for Employee")
            print("9. Get Payrolls for Period")
            print("10. Calculate Tax")
            print("11. Get Tax By Id")
            print("12. Get Tax for Employee")
            print("13. Get Tax for Year")
            print("14. Get Financial Record by ID")
            print("15. Add Financial Record")
            print("16. Get Financial Records for Employee")
            print("17. Get Financial Records for Date")
            print("18. Exit")

            choice = input(f"Select an option: ")
            print(f"\n")

            if choice == '1':
                self.add_employee()
            elif choice == '2':
                self.get_employee_by_id()
            elif choice == '3':
                self.get_all_employees()
            elif choice == '4':
                self.update_employee()
            elif choice == '5':
                self.remove_employee()
            elif choice == '6':
                self.get_payroll_by_id()
            elif choice == '7':
                self.generate_payroll()
            elif choice == '8':
                self.get_payroll_for_employee()
            elif choice == '9':
                self.get_payrolls_for_period()
            elif choice == '10':
                self.calculate_tax()
            elif choice == '11':
                self.get_tax_by_id()
            elif choice == '12':
                self.get_tax_for_employee()
            elif choice == '13':
                self.get_tax_for_year()
            elif choice == '14':
                self.get_financial_record_by_id()
            elif choice == '15':
                self.add_financial_record()
            elif choice == '16':
                self.get_financial_record_for_employee()
            elif choice == '17':
                self.get_financial_record_for_date()
            elif choice == '18':
                print("Exiting the system...")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    def add_employee(self):
        # Handles adding a new employee.
        try:
            employee_data = self.get_employee_details()
            if self.employee_service.add_employee(employee_data):  # Use the service instance
                print("Employee added successfully.")
            else:
                print("Failed to add employee.")
        except InvalidInputException as e:
            print(f"Invalid input: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_employee_by_id(self):
        # Gets all the details of the employee with specific employee id
        try:
            employee_id = input("Enter Employee ID :")
            employee = self.employee_service.get_employee_by_id(employee_id)  # Use the service instance
            if employee:
                print(employee)
            else:
                print(f"Employee with ID {employee_id} not found.")
        except EmployeeNotFoundException as e:
            print(f"Error: {str(e)}")
        except InvalidInputException as e:
            print(f"Invalid input: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_all_employees(self):
        # Gets details of all the employees
        try:
            employees = self.employee_service.get_all_employees()  # Use the service instance
            for employee in employees:
                print(employee)
                print(f"\nNext\n")
        except Exception as e:
            print(f"Error: {str(e)}")

    def update_employee(self):
        # Handles updating an existing employee.
        try:
            employee_data = self.get_employee_details_for_update()  # Collect employee details using helper function
            if self.employee_service.update_employee(employee_data):  # Use the service instance
                print("Employee updated successfully.")
            else:
                print("Failed to update employee.")
        except EmployeeNotFoundException as e:
            print(f"Error: {str(e)}")
        except InvalidInputException as e:
            print(f"Invalid input: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def remove_employee(self):
        # Handles removing an employee.
        try:
            employee_id = input("Enter Employee ID to remove: ")
            if self.employee_service.remove_employee(employee_id):  # Use the service instance
                print("Employee removed successfully.")
            else:
                print("Failed to remove employee.")
        except EmployeeNotFoundException as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_payroll_by_id(self):
        # Handles getting payroll by id
        try:
            payroll_id = int(input("Enter Payroll Id: "))
            payroll = self.payroll_service.get_payroll_by_id(payroll_id)  # Use the service instance
            if payroll:
                print(payroll)
            else:
                print(f"Payroll with ID {payroll_id} not found.")
        except PayrollGenerationException as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def generate_payroll(self):
        # Handles generating payroll for an employee.
        try:
            payroll_data = self.get_payroll_details()  # Collect payroll details using helper function
            if self.payroll_service.generate_payroll(payroll_data):  # Use the service instance
                print("Payroll generated successfully.")
            else:
                print("Failed to generate payroll.")
        except PayrollGenerationException as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_payroll_for_employee(self):
        # Handles getting payroll for a particular employee
        try:
            employee_id = int(input("Enter employee ID: "))
            payrolls = self.payroll_service.get_payrolls_for_employee(employee_id)  # Use the service instance
            for payroll in payrolls:
                print(payroll)
        except InvalidInputException as e:
            print(f"Invalid input: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_payrolls_for_period(self):
        # Handles getting payrolls for a period
        try:
            print("Enter dates for generating payroll for a particular period")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            payrolls = self.payroll_service.get_payrolls_for_period(start_date, end_date)  # Use the service instance
            for payroll in payrolls:
                print(payroll)
        except PayrollGenerationException as e:
             print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def calculate_tax(self):
        # Handles calculating tax for an employee
        try:
            employee_id = int(input("Enter Employee ID: "))
            tax_year = int(input("Enter Tax Year: "))
            if self.tax_service.calculate_tax(employee_id, tax_year):  # Use the service instance
                print("Tax calculated successfully.")
            else:
                print("Failed to calculate tax.")
        except TaxCalculationException as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_tax_by_id(self):
        # Handles getting tax by tax id
        try:
            tax_id = int(input("Enter Tax ID: "))
            tax = self.tax_service.get_tax_by_id(tax_id)  # Use the service instance
            if tax:
                print(tax)
            else:
                print(f"Tax with ID {tax_id} not found.")
        except InvalidInputException as e:
                print(f"Invalid input: {str(e)}")
        except Exception as e:
                print(f"Error: {str(e)}")

    def get_tax_for_employee(self):
        # Handles getting tax by employee id
        try:
            employee_id = int(input("Enter Employee ID: "))
            taxes = self.tax_service.get_taxes_for_employee(employee_id)  # Use the service instance
            for tax in taxes:
                print(tax)
        except InvalidInputException as e:
                print(f"Invalid input: {str(e)}")
        except Exception as e:
                print(f"Error: {str(e)}")

    def get_tax_for_year(self):
        # Handles getting tax by tax year
        try:
            tax_year = int(input("Enter Tax Year: "))
            taxes = self.tax_service.get_taxes_for_year(tax_year)  # Use the service instance
            for tax in taxes:
                print(tax)
        except InvalidInputException as e:
                print(f"Invalid input: {str(e)}")
        except Exception as e:
                print(f"Error: {str(e)}")

    def get_financial_record_by_id(self):
        # Handles getting financial record by record id
        try:
            record_id = int(input("Enter Record ID: "))
            record = self.financial_service.get_financial_record_by_id(record_id)  # Use the service instance
            if record:
                print(record)
            else:
                print(f"Financial record with ID {record_id} not found.")
        except FinancialRecordException as e:
                print(f"Error: {str(e)}")
        except InvalidInputException as e:
                print(f"Invalid input: {str(e)}")
        except Exception as e:
                print(f"Error: {str(e)}")

    def add_financial_record(self):
        # Handles adding a financial record.
        try:
            financial_data = self.get_financial_record_details()  # Collect financial record details
            if self.financial_service.add_financial_record(financial_data):  # Use the service instance
                print("Financial record added successfully.")
            else:
                print("Failed to add financial record.")
        except FinancialRecordException as e:
            print(f"Error: {str(e)}")
        except InvalidInputException as e:
            print(f"Invalid input: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_financial_record_for_employee(self):
        # Handles getting records for employee id
        try:
            employee_id = int(input("Enter Employee Id: "))
            records = self.financial_service.get_financial_records_for_employee(employee_id)  # Use the service instance
            for record in records:
                print(record)
        except FinancialRecordException as e:
            print(f"Error: {str(e)}")
        except InvalidInputException as e:
            print(f"Invalid input: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_financial_record_for_date(self):
        # Handles getting records for date
        try:
            record_date = input("Enter Date of Record: ")
            records = self.financial_service.get_financial_records_for_date(record_date)  # Use the service instance
            for record in records:
                print(record)
        except FinancialRecordException as e:
            print(f"Error: {str(e)}")
        except InvalidInputException as e:
            print(f"Invalid input: {str(e)}")
        except Exception as e:
            print(f"Error: {str(e)}")

    def get_employee_details(self):
        # Helper function to collect employee details from the user.
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        gender = input("Enter Gender: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")
        position = input("Enter Position: ")
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
        return (first_name, 
                last_name, 
                dob, 
                gender, 
                email, 
                phone, 
                address, 
                position, 
                joining_date)
    
    def get_employee_details_for_update(self):
        # Helper function to collect employee update details from the user.
        employee_id = input("Enter Employee ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        gender = input("Enter Gender: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")
        position = input("Enter Position: ")
        joining_date = input("Enter Joining Date (YYYY-MM-DD): ")
        
        # Return employee data as a dictionary
        return {
            'employee_id': employee_id,
            'first_name': first_name,
            'last_name': last_name,
            'dob': dob,
            'gender': gender,
            'email': email,
            'phone': phone,
            'address': address,
            'position': position,
            'joining_date': joining_date,
        }
    
    def get_payroll_details(self):
        # Helper function to collect payroll details from the user.
        employee_id = input("Enter Employee ID: ")
        start_date = input("Enter Payroll Start Date (YYYY-MM-DD): ")
        end_date = input("Enter Payroll End Date (YYYY-MM-DD): ")
        basic_salary = float(input("Enter Basic Salary: "))
        overtime_pay = float(input("Enter Overtime Pay: "))
        deductions = float(input("Enter Deductions: "))
    
        # Return payroll data as a tuple (like employee_data in add_employee)
        return (employee_id, 
                start_date, 
                end_date, 
                basic_salary, 
                overtime_pay, 
                deductions)

    def get_financial_record_details(self):
        # Helper function to collect financial record details from the user.
        employee_id = input("Enter Employee ID: ")
        record_date = input("Enter Record Date: ")
        description = input("Enter Description: ")
        amount = float(input("Enter Amount: "))
        record_type = input("Enter Record Type (income/expense/tax): ")
    
        if record_type not in ["income", "expense", "tax"]:
            raise InvalidInputException("Invalid record type. Must be 'income', 'expense', or 'tax'.")
    
        # Return financial record data as a tuple (like employee_data in add_employee)
        return (employee_id, 
                record_date,
                description, 
                amount, 
                record_type)
    

def main():
    # Start the Payroll Management System
    payroll_manager = PayrollManagementSystem()
    payroll_manager.display_menu()

if __name__ == "__main__":
    main()
