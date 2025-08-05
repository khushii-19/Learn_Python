def reverse(n):
    sum = 0
    while(n>0):
        last_digit = n%10
        sum = (sum*10)+last_digit
        n = n//10
    return sum
a = reverse(int(input("Enter a number: ")))
print(a)   


