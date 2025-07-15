# Write a program to find whether a given username contains less than 10
# characters or not.

name = input("Enter your name")
if(len(name)<10):
    print("yes",len(name))
else:
    print("no",len(name))    