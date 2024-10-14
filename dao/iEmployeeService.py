from abc import ABC, abstractmethod

class IEmployeeService(ABC):
    # get the employee by their employee id
    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    # get all the employees from list
    @abstractmethod
    def get_all_employees(self):
        pass

    # add a new employee to the database
    @abstractmethod
    def add_employee(self, employee_data):
        pass

    # update the details abour an employee in tge database
    @abstractmethod
    def update_employee(self, employee_data):
        pass

    # remove an employee from the database
    @abstractmethod
    def remove_employee(self, employee_id):
        pass
