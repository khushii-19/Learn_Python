# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern(n):
    if(n==0):
        return()
    else:
       print("*"*n)
       pattern(n-1)  #ab 2 baar chalega na basically ye iterate krne ka n-- krne ka tareeka h function ko usi k andar call krlia ab same cheez krega

pattern(5)       