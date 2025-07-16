# Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if(n<=0):
        print("Not a natural number", n)
    elif(n==1):   #base condition is important in recursion
        return 1    
    else:
        return(sum(n-1)+n)    

print(sum(n=int(input("Enter a number"))))