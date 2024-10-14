class FinancialRecordException(Exception):
    
    # Raised when there is an issue with financial record management.
    def __init__(self, message="Error managing financial records"):
        self.message = message
        super().__init__(self.message)
