#  7. FACTORIAL USING RECURSION
def factorial(n):
    # Base condition
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)  #this factorial function will keep calling itself and solve it recursively like 3 * factorial(2) = 3*2*factorial(1) = 3*2*1

print("Factorial of 5 is:", factorial(5))  # Output: 120


#  8. TABLE USING FUNCTION
def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

print_table(4)


#  9. NESTED FUNCTION CALL
def outer():
    print("Inside outer function")

    def inner():
        print("Inside inner function")

    inner()  # calling inner inside outer

outer()