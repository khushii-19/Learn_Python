# Create a class “Programmer” for storing information of few programmers
# working at Microsoft
class programmer:
     company = "Microsoft"
     def __init__(self,name,salary):
          self.name = name 
          self.salary = salary

m1 = programmer("Khushi", "25,00,000")
m2 = programmer("atharv", "30,00,000")
print(m1.name,m1.salary,m1.company)
print(m2.name,m2.salary,m2.company)
