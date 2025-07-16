# Write a program to find whether a given number is prime or not.

num = int(input("Enter a number: "))
if(num<=1):
    print("Not a prime number")

else:
   for i in range(2, num):
     if(num%i==0):
         print("not a Prime number",num)
         break
   else:    
      print("it's a prime number",num)

