class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

    @property  #using this we can return anything
    def name(self):
        return f"{self.fname} {self.lname}"  #jab e.name print karaya then it returns Khushi Gupta to setter and it splits it as first and last name so that if any one of it changes we can change it directlky using e.fname = atharv
    
    @name.setter #jo getter mae likha h vo @ lagake set
    def name (self,value): #same function jo setter mae h gett kia h
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Khushi Gupta"   #(name can be used as a variable not a method)
print(e.fname, e.lname)
e.fname = "Atharv"
print(e.fname,e.lname)

e.show()
