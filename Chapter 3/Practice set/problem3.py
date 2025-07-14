# Write a program to detect double space in a string

a = "Hey this is  me"
b = a.find("  ")
print (b)

# returns -1 if no double space found

# Replace the double space from problem 3 with single spaces.

print(a.replace("  ", " "))

# here new string is created a is as it is strings are immutable cant be changed
print(a)