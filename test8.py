#Created a class
class Dog:
    def __init__(self,breed,name):
        self.breed = breed
        self.name = name
# Created a method
    def f1(self):
        print("I am a " + self.breed + "\nMy name is " + self.name)

D1 = Dog("Boxer", "'Ace'")
D1.f1()
    
