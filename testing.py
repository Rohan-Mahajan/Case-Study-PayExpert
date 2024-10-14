import unittest
from unittest.mock import MagicMock
from datetime import datetime
from entity.payroll import Payroll
from dao.payrollService import PayrollService
from dao.taxService import TaxService
from exceptions.invalidInputException import InvalidInputException
from exceptions.payrollGenerateException import PayrollGenerationException


class PayrollServiceTestCase(unittest.TestCase):

    def setUp(self):
        # Initialize PayrollService and TaxService before each test
        self.payroll_service = PayrollService()
        self.tax_service = TaxService()

    def test_CalculateNetSalaryAfterDeductions(self):
        # Test calculation of net salary
        basic_salary = 50000
        overtime_pay = 2000
        deductions = 5000

        net_salary = self.payroll_service.calculate_net_salary(basic_salary, overtime_pay, deductions)

        expected_net_salary = basic_salary + overtime_pay - deductions
        self.assertEqual(net_salary, expected_net_salary)

    def test_CalculateGrossSalaryForEmployee(self):
        # Test calculation of gross salary
        basic_salary = 60000
        overtime_pay = 2500

        gross_salary = self.payroll_service.calculate_gross_salary(basic_salary, overtime_pay)

        expected_gross_salary = basic_salary + overtime_pay
        self.assertEqual(gross_salary, expected_gross_salary)

    def test_VerifyTaxCalculationForHighIncomeEmployee(self):
        # Test tax calculation for high-income employee
        taxable_income = 100000
        tax_year = 2024  # Provide a valid tax year
    
        tax_amount = self.tax_service.calculate_tax(tax_year, taxable_income)
    
        expected_tax_amount = 0.1 * taxable_income  # Assuming 10% tax for high income
        self.assertEqual(tax_amount, expected_tax_amount)


    def test_process_payroll_for_multiple_employees(self):
        # Test payroll processing for multiple employees
        employee_ids = [1, 2, 3]
        start_date = '2023-01-01'
        end_date = '2023-01-31'

        # Mock multiple payroll generations
        self.payroll_service.generate_payroll = MagicMock(side_effect=[5000, 5500, 6000])

        payrolls = [self.payroll_service.generate_payroll(emp_id, start_date, end_date) for emp_id in employee_ids]
        
        self.assertEqual(payrolls, [5000, 5500, 6000], "Payroll should be processed correctly for multiple employees.")
    
    def test_verify_error_handling_for_invalid_employee_data(self):
        # Test error handling for invalid employee data
        invalid_payroll = Payroll(
            payroll_id=888,  # invalid
            employee_id=9999,  # Assuming 9999 is an invalid ID
            start_date=datetime(2024, 10, 1),
            end_date=datetime(2024, 10, 31),
            basic_salary=50000,
            overtime_pay=5000,
            deductions=2000,
            net_salary=None
        )

        self.payroll_service.generate_payroll = MagicMock(side_effect=PayrollGenerationException("Payroll not generated properly"))

        with self.assertRaises(PayrollGenerationException) as context:
            self.payroll_service.generate_payroll(invalid_payroll)

        self.assertEqual(
            str(context.exception), "Payroll not generated properly",
            "Error message did not match the expected output."
        )

if __name__ == '__main__':
    unittest.main()
