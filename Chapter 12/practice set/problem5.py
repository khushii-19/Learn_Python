n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
with open("Chapter 12/practice set/tables.txt", "a") as f:
    f.write(f"Table of {n}: {str(table)} \n")