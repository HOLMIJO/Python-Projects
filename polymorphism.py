#Parent Class User
class User:
    name = "Joseph Holmin"
    email = "holminj@icloud.com"
    password = "SecretPW1"

    def getLogin(self):
        nameID = input("Enter your name: ")
        emailID = input("Enter your email: ")
        passwordID = input("Enter your password: ")
        if (emailID == self.email and passwordID == self.password):
            print("Hello {}!".format(nameID))
        else:
            print("The email or password given is incorrect.")

#Child class Worker1
class Worker1(User):
    department = "Sales"
    pin = "1205"

# Employees use a pin number, not a password

    def getLogin(self):
        nameID = input("Enter your name: ")
        emailID = input("Enter your email: ")
        pinID = input("Enter your PIN: ")
        if (emailID == self.email and pinID == self.pin):
            print("Hello {}!".format(nameID))
        else:
            print("The email or PIN given is incorrect")

#Child class Contractor1
class Contractor1(User):
    eqID = "PC-1080P"
    locationID = "Branch-2456"
#Contractors enter name, equipment ID, location ID and a PIN
    def getLogin(self):
        nameID = input("Enter your name: ")
        eqID = input("Enter your equipment ID: ")
        locationID = input("Enter your location: ")
        pinID = input("Enter your PIN: ")
        if (eqID == self.eqID and pinID == self.pin and locationID == self.locationID):
            print("Hello {}!".format(nameID))
        else:
            print("The information you entered is incorrect")
        
