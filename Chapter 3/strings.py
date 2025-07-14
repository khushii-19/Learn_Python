# Length -calculates length_ len(str)
str = "harry"
print(len(str)) # Output: 5

# Endswith - checks - str.endswith()
str = "harry"
print(str.endswith("rry")) # Output: True

# Count - counts given int or string-  str.count("c")
str = "harry"
count = str.count("r")
print(count) # Output: 2

# Captiliazize - firat word -  str.captalize()
str = "harry"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry"

# find - find index position- str.find(k)   retunrs -1 if nothing relevant found
str = "harry"
index = str.find("rr")
print(index) # Output: 2

# replace - replace that string - str.replace(r, l)
str = "harry"
replaced_string = str.replace("r", "l")
print(replaced_string) # Output: "hally"