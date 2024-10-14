class EmployeeNotFoundException(Exception):

    # Raised when attempting to access or perform operations on a non-existing employee.
    def __init__(self, message="Employee not found"):
        self.message = message
        super().__init__(self.message)
