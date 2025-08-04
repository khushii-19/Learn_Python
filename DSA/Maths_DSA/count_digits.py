#given the number n find out how many digits present in a number

def count_num(n):
    count = 0
    while(n>0):
        a = n%10
        count += 1
        n = n//10  #integer division
    return(count)   

a = count_num(int(input("Enter a number: ")))
print(a)
