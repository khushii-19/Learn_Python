class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")  #isse hume object pass krte hue print nhi krna [ada class k andar he function ban gya jo ki print kr rha h class se leke ]

    @staticmethod
    def greet():
        print("Good morning")

   #now why should we pass anything to it when its not retunring anything just printing so we made it static method     


harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo() 
# Employee.getInfo(harry)   this is same as above when we defined getinfo and didnt passed self i mean we created function and didnt pass an attribute it was then too showing that u have passed because its passing so we need to write self we can write self kk, cr anything anyname aas attribute because it takes value when its called along object

