try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyyy")  #if printing value error print can be directly used here but it works same as exception
    print(v)
    
except Exception as e:
    print(e) 

print("Thank You")



