from datetime import date

class Person:
    def __init__(self, name, age): #self holds the object reference.
        self.name = name
        self.age = age

    @classmethod #on using this annotation, we transfer the ownership of the method to the class instead of the object.
    def frombirthyear(cls, name, birthyear): #cls is a parameter that holds the class object.
        return cls(name, date.today().year-birthyear) #here we are returning the reference for the class object which can be stored in a variable.

    def display(self):
        print(self.name + "'s age is: "+str(self.age))


person = Person("Happy", 23) #person holds reference to the object which has a name happy and age 23.
person.display()
