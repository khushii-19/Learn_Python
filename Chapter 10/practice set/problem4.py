# Add a static method in problem 2, to greet the user with hello

class calculator:
    def __init__(self,n):
        self.n=n

    @staticmethod
    def greet():
        print("Good morning")    

    def square(self):
        print(f"sqaure of number {self.n} is {self.n*self.n}")   

    def cube(self):
        print(f"cube of number {self.n} is {self.n*self.n*self.n}")

    def sqaure_root(self):
        print(f"square root of number {self.n} is {self.n*1/2}")    


s = calculator(4)
s.greet()
s.square()
s.cube()
s.sqaure_root()
