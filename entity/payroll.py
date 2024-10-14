class Payroll:
    def __init__(self, payroll_id=None, employee_id=None, start_date=None, end_date=None, basic_salary=None, overtime_pay=None, deductions=None, net_salary=None):
        self.__payroll_id = payroll_id
        self.__employee_id = employee_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__basic_salary = basic_salary
        self.__overtime_pay = overtime_pay
        self.__deductions = deductions
        self.__net_salary = net_salary

    # Getters methods
    def get_payroll_id(self):
        return self.__payroll_id

    def get_employee_id(self):
        return self.__employee_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_basic_salary(self):
        return self.__basic_salary

    def get_overtime_pay(self):
        return self.__overtime_pay

    def get_deductions(self):
        return self.__deductions

    def get_net_salary(self):
        return self.__net_salary

    # Setter methods
    def set_payroll_id(self, payroll_id):
        self.__payroll_id = payroll_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_basic_salary(self, basic_salary):
        self.__basic_salary = basic_salary

    def set_overtime_pay(self, overtime_pay):
        self.__overtime_pay = overtime_pay

    def set_deductions(self, deductions):
        self.__deductions = deductions

    def set_net_salary(self, net_salary):
        self.__net_salary = net_salary


    def __str__(self):
        return (f"Payroll ID: {self.__payroll_id}\n"
                f"Employee ID: {self.__employee_id}\n"
                f"Start Date: {self.__start_date}\n"
                f"End Date: {self.__end_date}\n"
                f"Basic Salary: {self.__basic_salary}\n"
                f"Overtime Pay: {self.__overtime_pay}\n"
                f"Deductions: {self.__deductions}\n"
                f"Net Salary: {self.__net_salary}")