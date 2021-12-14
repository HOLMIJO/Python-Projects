# Created a class Protected and assigned a private and protected variable as such
  class Protected:
       def __init__(self):
            self.__privateVar = 25  # This is private, denoted bt double underline
            self._protectedVar = 125  # This is protected, denoted by a single underline

        def getPrivate(self):
            print(self.__privateVar)  # Prints private variable
            print(self._protectedVar)  # Prints protected variable

        def setPrivate(self, private):  # Sets private variable as private
            self.__privateVar = private

obj = Protected()  # Object links to Protected class
obj.getPrivate()  # Object gets protected variable
obj.setPrivate(18)  # Object sets private variable to new value
obj.getPrivate()  # Object gets value from protected variable
