
# 1. Empty tuple
a = ()
print("Empty tuple:", a)

# 2. Tuple with one element (comma is necessary)
a = (1,)
print("Single-element tuple:", a)

# 3. Tuple with multiple elements
a = (1, 7, 2)
print("Multi-element tuple:", a)

# 4. count() - Counts how many times 1 appears
count_1 = a.count(1)
print("a.count(1):", count_1)  # Output: 1

# 5. index() - Finds the index of the first occurrence of 1
index_1 = a.index(1)
print("a.index(1):", index_1)  # Output: 1
