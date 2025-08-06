#  print all divisors of a number

def divisors(n):
    result = []
    for i in range(1,n+1):
        if(n%i==0):
            result.append(i) #if want list
            # return i #return exists the function
    return result
a = divisors(int(input("Enter a number: ")))
print(a)           