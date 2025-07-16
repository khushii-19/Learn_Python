# FOR LOOP: Basic usage
# -----------------------------

print("FOR LOOP: Looping through list")
numbers = [1, 7, 8]
for num in numbers:
    print(num)
print()

# -----------------------------
# FOR LOOP with range()
# -----------------------------

print("FOR LOOP with range(): Printing 0 to 6")
for i in range(0, 7):
    print(i)
print()

# -----------------------------
# FOR LOOP with ELSE
# -----------------------------

print("FOR LOOP with ELSE")
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)
else:
    print("Loop completed!\n")