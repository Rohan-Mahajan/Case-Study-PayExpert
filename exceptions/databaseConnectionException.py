class DatabaseConnectionException(Exception):
    
    # Raised when there is a problem establishing or maintaining a connection with the database.
    def __init__(self, message="Failed to connect to the database"):
        self.message = message
        super().__init__(self.message)
