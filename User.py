# The User class is the parent class
# All of it's attributes are available to the child classes
class User:
    # Define the attributes of the class
    name = "No Name Provided"
    email = ""
    password = "1234abcd"
    account = 0
    # This initialization attaches arguments for creating object user.

    def __init__(self, name, email, password, account):
        self.name = name
        self.email = email
        self.password = password
        self.account = account

    # Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}".format(self.name))
        else:
            print("You are not authorized for this page.")


# Outside of the class you would create an instance of the User class
new_user = User()
# Call the login method using the new object
new_user.login()

# Employee is a child class with it's own attributes


class Employee(User):
    base_pay = 15.00
    department = 'General'


# Customer is a child class with it's own attributes.
class Customer(User):
    mailing_address = ' '
    mailing_list = True
