class InvalidInputException(Exception):
    
    # Raised when input data doesn't meet the required criteria.
    def __init__(self, message="Invalid input provided"):
        self.message = message
        super().__init__(self.message)
