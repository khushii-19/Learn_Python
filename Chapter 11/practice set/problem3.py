# Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.

class Employee:
    salary = 250
    increment = 20
    
    @property
    def salaryAfterIncrement(self):
        return f"salary after increment {self.salary + self.salary *(self.increment)/100}  "
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) -1)*100  #salary = 1+increment*salary/100


d = Employee()
print(d.salaryAfterIncrement)
d.salaryAfterIncrement = 300.0 #getter salary return krke dera h setter ko
print(d.increment)

