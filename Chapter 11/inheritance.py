class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

#instead of above we used inheritance
class Programmer(Employee):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

print(a.company , b.company)
# Even though Programmer inherits from Employee, it overrides the company attribute with a new value.

# Programmer automatically has access to show() method from Employee
a = Employee()
a.name = "Khushi"
a.salary = 50000

b = Programmer()
b.name = "Ayush"
b.salary = 70000
b.language = "Python"  #when we gave this it overirides employee and update name and do what show function in employee do jo vo kaam kr rha h usko print krTA H

b.show()           # inherited from Employee
b.showLanguage()   # from Programmer class


