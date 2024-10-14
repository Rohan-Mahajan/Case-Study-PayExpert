class PropertyUtil :
    
    @staticmethod
    def getConnectionString() :
        return (
            'Driver={SQL Server};'
            'Server=MYIDEAPAD\SQLEXPRESS;'  
            'Database=payexpert;'
            'Trusted_Connection=yes;'
        )