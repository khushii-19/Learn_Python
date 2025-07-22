# . Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.

class two_D_vector:
     def __init__(self,i,j):
          self.i = i
          self.j = j     

     def show(self):
          print(f"The vector is {self.i}i , {self.j}j") 

class three_D_vector(two_D_vector):
     def __init__(self,i,j,k):   #this will use i j defined before
          super().__init__(i,j)
          self.k = k
     def show(self):
          print(f"The vector is {self.i}i , {self.j}j, {self.k}k")     

a = two_D_vector(1,2)
a.show()  #constructors banane se ek step kam hojata h methods se vrna pahle object se class initialise kro then method mae value pass kro
b = three_D_vector(3,4,8)      
b.show()
