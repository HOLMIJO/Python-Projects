
class Protected:
    def __init__(self):
        self.__privateVar = 25
        self._protectedVar = 125

    def getPrivate(self):
        print(self.__privateVar)
        print(self._protectedVar)

    def setPrivate(self, private):
        self.__privateVar = private

obj = Protected()
obj.getPrivate()
obj.setPrivate(18)
obj.getPrivate()

