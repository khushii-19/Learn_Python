# Write a python function which converts inches to cms.

#  Function to convert inches to centimeters
def inches_to_cm(inches):
    return inches * 2.54

# 🔹 Taking input from user
inches = float(input("Enter length in inches: "))

# 🔹 Calling the function
centimeters = inches_to_cm(inches)

# 🔹 Display the result
print(f"{inches} inches is equal to {centimeters} centimeters")