# BREAK statement: Exit when number is 3
# -----------------------------

print("BREAK statement demo")
for i in range(10):
    print(i)
    if i == 3:
        print("Breaking the loop at i = 3")
        break
print()

# -----------------------------
# CONTINUE statement: Skip printing when i == 2
# -----------------------------

print("CONTINUE statement demo")
for i in range(5):
    if i == 2:
        print("Skipping i =", i)
        continue
print()

# -----------------------------
# PASS statement: Placeholder logic
# -----------------------------

print("PASS statement demo")
colors = ["red", "green", "blue"]
for color in colors:
    if color == "green":
        pass  # Placeholder for future code
    else:
        print("Color is:", color)

print("\nProgram End.")