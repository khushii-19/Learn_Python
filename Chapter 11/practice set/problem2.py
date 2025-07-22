# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# # ‘Pets’. Add a method ‘bark’ to class ‘Dog’.

class Animals:
    pass
class Pets:
    pass
class Dog(Pets):
    def bark(self,dog):
        self.dog = dog
        print(f"{self.dog},barks")

d = Dog()
d.bark("Labra")   #ye constructor ki traha direct pass ni krsakte pahle object define then method and method la bhi pahle likhna hoga self.dog krke
