class Users:
    #variable declaration
    first_name = None
    last_name = None
    email = None
    phone_number = None
    zip_code = None
    membership_code = None

    #constructor
    def __init__(self, first_name, last_name, email, phone_number, zip_code, membership_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.zip_code = zip_code
        self.membership_code = membership_code

