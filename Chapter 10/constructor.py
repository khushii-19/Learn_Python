class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # its constructor dunder method which is automatically called it dont need to call it starts with (__) DOUBLE UNDERSCORE and as it calls itself as a function we need to pass and attributes which object will use to pass 
        self.name = name  #name ki jagah object mae jo name hoga vo aajayega
        self.salary = salary
        self.language = language
        print("I am creating an object")

        #Jo bhi aap values dete ho (name, salary, language) — wo self.<attribute> ke through object me store ho jaati hain.


harry = Employee("Harry", 1300000, "JavaScript")  #ye contructor ko follow krega and constructor ne overwrite krdia class attributes ko
# harry.name = "Harry"
print(harry.name, harry.salary, harry.language)  #ab ye jo constructor mae self k saath diye and object mae vo pass krdiye unhe print krega


# rohan = Employee()

