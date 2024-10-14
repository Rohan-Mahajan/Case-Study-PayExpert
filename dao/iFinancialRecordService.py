from abc import ABC, abstractmethod

class IFinancialRecordService(ABC):

    # Add a new financial record for a specific employee
    @abstractmethod
    def add_financial_record(self, employee_id, description, amount, record_type):
        pass

    # Retrieve a financial record by its unique record ID
    @abstractmethod
    def get_financial_record_by_id(self, record_id):
        pass

    # Get all financial records associated with a particular employee
    @abstractmethod
    def get_financial_records_for_employee(self, employee_id):
        pass

    # Retrieve all financial records for a specific date
    @abstractmethod
    def get_financial_records_for_date(self, record_date):
        pass