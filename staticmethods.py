class Dates:
    def __init__(self, date):
        self.date = date

    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date): #no class or object reference present. You also need to pass a value as it cannot access instance variables.
        return date.replace("/", "-")  #here we are returning an object


date = Dates("15-12-2016")  #object created and its reference is being stored in dates.
datefromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(datefromDB)
print(date.getDate())

if date.getDate() == dateWithDash:
    print("Equal")
else:
    print("Unequal")

#static methods work as utility methods were we can use the same method for a task multiple times by parameterizing it.