# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class khushi:
    a = 9  #class attribute

b = khushi()
b.a = 0   #instance attribute
print(b.a)