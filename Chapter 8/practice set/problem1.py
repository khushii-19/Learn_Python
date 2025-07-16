# Write a program using functions to find greatest of three numbers

def greatest_number(n1,n2,n3):
    if(n1>n2 and n1>n3):
        print(f"{n1} is the greatest number")
    elif(n2>n1 and n2>n3):
        print(f"{n2} is the greatest number")
    else:
        print(f"{n3} is the greatest number")

greatest_number(n1= int(input("enter 1 number : ")),
                n2= int(input("enter 2 number : ")),
                n3= int(input("enter 3 number : ")))