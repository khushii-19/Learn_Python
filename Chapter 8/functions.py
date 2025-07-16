# 1. BASIC USER-DEFINED FUNCTION
def greet_user():
    # Function definition - No parameters
    print("Good day!")

# Function call
greet_user()  # Output: Good day!


#  2. FUNCTION WITH ARGUMENTS & RETURN VALUE
def greet(name):
    # Function that takes a name and returns greeting
    greeting = "Hello " + name
    return greeting   #returning means this function can store or pass its value to some other variable

a = greet("Harry")
print(a)  # Output: Hello Harry


#  3. DEFAULT PARAMETERS
def greet_default(name="Stranger"):
    print("Hi,", name)

greet_default()         # No argument passed → Output: Hi, Stranger
greet_default("Khushi") # Argument passed → Output: Hi, Khushi


#  4. BUILT-IN FUNCTIONS
print(len("Hello"))     # len() is a built-in function → Output: 5
print(max(3, 5, 2))     # max() is also built-in → Output: 5


#  5. FUNCTION TO ADD TWO NUMBERS
def add(a, b):
    return a + b

result = add(10, 15)
print("Sum is:", result)  # Output: Sum is: 25


#  6. FUNCTION TO CHECK EVEN OR ODD
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("7 is", check_even_odd(7))  # Output: 7 is Odd