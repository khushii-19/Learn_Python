class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")  #its a class method so only follow class attribute even after channging instance attribute

e = Employee()
e.a = 45

e.show()