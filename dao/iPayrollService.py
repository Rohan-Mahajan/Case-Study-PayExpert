from abc import ABC, abstractmethod

class IPayrollService(ABC):

    # generate the payroll for employee id
    @abstractmethod
    def generate_payroll(self, employee_id, start_date, end_date):
        pass

    # get payroll for perticular payroll id
    @abstractmethod
    def get_payroll_by_id(self, payroll_id):
        pass

    # get payroll for perticular employee id
    @abstractmethod
    def get_payrolls_for_employee(self, employee_id):
        pass

    # get payrolls for a particular period of time
    @abstractmethod
    def get_payrolls_for_period(self, start_date, end_date):
        pass
