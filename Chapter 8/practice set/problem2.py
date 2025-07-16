# Write a python program using function to convert Celsius to Fahrenheit.

def convert(c):
    return (c* 9/5) + 32
f = convert(c = float(input("Enter the temperature in celcius")))
print(f"Temperature in Faherenheit: {round (f ,2)}")


