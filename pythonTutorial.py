

#
# Python:   3.10.0
#
# Author: Joseph Holmin
#
# Purpose: The Tech Academy - Python Course, Creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable,
#           return variable _means that we are returning the variable to
#           back to the calling function.
#
#



def start():
    f_name = "Joseph"
    l_name = "Holmin"
    age = 52
    gender = "Male"
    get_info(f_name,l_name,age,gender)


def get_info(f_name,l_name,age,gender):
    print("My name is {} {}. I am a {} yearold {}.".format(f_name,l_name,age,gender))






if __name__ == "__main__":
    start()
