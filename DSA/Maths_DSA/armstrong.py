#check a number is armstrong or not armstrong = n = (digit)^3 + ...all digits

def reverse(n):
    sum = 0
    m=n
    while(n>0):
        last_digit = n%10
        sum = ( sum)+ ((last_digit)*(last_digit)*(last_digit))
        n = n//10

    if(m==sum):
        return True
    else:
        return False

a = reverse(int(input("Enter a number: ")))
print(a)   