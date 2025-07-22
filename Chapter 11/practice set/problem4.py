# Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.

class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2):
        return Complex(self.r + c2.r, self.i + c2.i) 
#        Ek naya object banao Complex class ka.c2.r aur c2.i isliye likh paaye kyunki:c2 ek object hai Complex class ka
#        Uske real aur imaginary parts, dono complex numbers ke real + real, imaginary + imaginary kar do. and vo complex form mae he return hoga isliye 

    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"  #   <__main__.Complex object at 0x000001DD3BE68E10> to make this output string for this class
    #jab bhi print likhenge ye jayega str mae connvert krne
#     self = c1 → jisme r = 1 and i = 2
# c2 = c2 → jisme r = 3 and i = 4
# To return hoga:
# Complex(1 + 3, 2 + 4) → Complex(4, 6)
# Ek naya object ban gaya Complex(4, 6). Is object ke andar:
# self.r = 4
# self.i = 6
#  Step 2: print(...) calls __str__ of that returned object
# def __str__(self):
#     return f"{self.r} + {self.i}i"
# Yahaan self us new object ko refer karta hai jo Complex(4,6) tha.
# self.r → 4  
# self.i → 6  
# Aur output ban gaya:
# "4 + 6i"

c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1 + c2)
print(c1*c2)

