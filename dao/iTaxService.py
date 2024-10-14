from abc import ABC, abstractmethod

class ITaxService(ABC):

    # Calculate the tax for a specific employee and tax year
    @abstractmethod
    def calculate_tax(self, employee_id, tax_year):
        pass

    # Retrieve a tax record by its unique tax ID
    @abstractmethod
    def get_tax_by_id(self, tax_id):
        pass

    # Get all tax records associated with a particular employee
    @abstractmethod
    def get_taxes_for_employee(self, employee_id):
        pass

    # Retrieve all tax records for a specific tax year
    @abstractmethod
    def get_taxes_for_year(self, tax_year):
        pass