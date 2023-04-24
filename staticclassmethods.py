from datetime import date


class Person:
    def __init__(self, name, age):  # self holds the current object reference.
        self.name = name
        self.age = age

    @classmethod  # on using this annotation, we transfer the ownership of the method to the class instead of the object.
    def frombirthyear(cls, name, birthyear):
        print(cls) # cls is a parameter that holds the class reference.
        return cls(name, date.today().year - birthyear)  # new object is being created to be stored in a variable.

    def display(self):
        print(self)
        print(self.name + "'s age is: " + str(self.age))


person = Person("Happy", 23)  # person holds reference to the object which has a name happy and age 23.
person.display()
person2 = Person.frombirthyear("Laughy", 2006)  # you can also call it using the class name because it is a class method.
person2.display()

#  we have 2 methods tp enter the age. Either enter the age directly or enter your birth year. Hence we have 2 different methods to accomplish the same task in 2 different ways.
#  cls holds a new object everytime. hence we can approach a problem in multiple ways using class methods.