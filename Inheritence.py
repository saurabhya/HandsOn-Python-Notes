class Employee(object):
    numEmployee = 0
    def __init__(self,name, rate):
        self.owed = 0
        self.name = 0
        self.rate = rate
        Employee.numEmployee += 1
    
    def __del__(self):
        Employee.numEmployee -= 1
    
    def hours(self,numHours):
        self.owed += numHours*self.rate
        return ("%.2f hours worked" %numHours)
    
    def pay(self):
        self.owed = 0
        return ("payed %s"%self.name)

class specialEmployee(Employee):
    def __init__(self, name, rate, bonus):
        Employee.__init__(self, name, rate) # calls the base classes
        self.bonus = bonus

    def hours(self, numHours):
        self.owed += numHours*self.rate*2
        return ("%.2f hours wroked"%numHours)

####################################################################################################################

# Example : issubclass() to check whether a class is a subclass of another class 
# Example : isinstance() to check if an object belongs to a class or not

print(issubclass(specialEmployee, Employee))
print(issubclass(Employee, specialEmployee))

d = specialEmployee("packt", 20, 100)
b = Employee("packt", 20)

print(isinstance(b, specialEmployee))
print(isinstance(b, Employee))


