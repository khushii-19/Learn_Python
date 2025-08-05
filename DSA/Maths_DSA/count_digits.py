#given the number n find out how many digits present in a number

import math
def count_num(n):
    count = (int)(math.log10(n)+1)   #log10 also reducing the expression
    # while(n>0):
    #     a = n%10
    #     count += 1
    #     n = n//10  #integer division
    return(count)   

a = count_num(int(input("Enter a number: ")))
print(a)
