class PayrollGenerationException(Exception):
    """
    Raised when there is an issue with generating payroll for an employee.
    """
    def __init__(self, message="Failed to generate payroll for the employee"):
        self.message = message
        super().__init__(self.message)
