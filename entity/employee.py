from datetime import date

class Employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, dob=None, gender=None, email=None, phone=None, address=None, position=None, joining_date=None, termination_date=None):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__gender = gender
        self.__email = email
        self.__phone = phone
        self.__address = address
        self.__position = position
        self.__joining_date = joining_date
        self.__termination_date = termination_date

    # Getter methods
    def get_employee_id(self):
        return self.__employee_id
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name

    def get_dob(self):
        return self.__dob

    def get_gender(self):
        return self.__gender

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_address(self):
        return self.__address

    def get_position(self):
        return self.__position

    def get_joining_date(self):
        return self.__joining_date

    def get_termination_date(self):
        return self.__termination_date

    # setter methods
    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id
    
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_dob(self, dob):
        self.__dob = dob

    def set_gender(self, gender):
        self.__gender = gender

    def set_email(self, email):
        self.__email = email

    def set_phone(self, phone):
        self.__phone = phone

    def set_address(self, address):
        self.__address = address

    def set_position(self, position):
        self.__position = position

    def set_joining_date(self, joining_date):
        self.__joining_date = joining_date

    def set_termination_date(self, termination_date):
        self.__termination_date = termination_date

    # Additional Method to calculate the age of employe
    def calculate_age(self):
        birthdate = date.fromisoformat(self.__dob)
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return age
    
    def __str__(self):
        return (f"Employee ID: {self.__employee_id}\n"
                f"Name: {self.__first_name} {self.__last_name}\n"
                f"DOB: {self.__dob}\n"
                f"Gender: {self.__gender}\n"
                f"Email: {self.__email}\n"
                f"Phone: {self.__phone}\n"
                f"Address: {self.__address}\n"
                f"Position: {self.__position}\n"
                f"Joining Date: {self.__joining_date}\n"
                f"Termination Date: {self.__termination_date}\n")