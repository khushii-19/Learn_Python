# Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class calculator:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"sqaure of number {self.n} is {self.n*self.n}")   

    def cube(self):
        print(f"cube of number {self.n} is {self.n*self.n*self.n}")

    def sqaure_root(self):
        print(f"square root of number {self.n} is {self.n*1/2}")    


s = calculator(4)
s.square()
s.cube()
s.sqaure_root()