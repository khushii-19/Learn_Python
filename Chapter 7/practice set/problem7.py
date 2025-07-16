# Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3

n = int(input("Enter a number : "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*((2*i)-1),end=" ")
    print("") #Print an empty line → i.e., just go to the next line because we used end that will keep printing in the same line 
    # if we used \n then it will create gap in between lines so just to change line