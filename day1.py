class Employee1:
    def __init__(self, name, base_pay):
        print('Parent class')
        self.name = name
        self.base_pay = base_pay

    def get_pay(self):
        print('Executed Employee1')
        x = self.base_pay
        return x

    def get_name(self):
        return self.name
