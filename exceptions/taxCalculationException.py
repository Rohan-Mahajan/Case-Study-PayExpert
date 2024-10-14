class TaxCalculationException(Exception):
    
    # Raised when there is an error in calculating taxes for an employee.
    def __init__(self, message="Error in tax calculation"):
        self.message = message
        super().__init__(self.message)
