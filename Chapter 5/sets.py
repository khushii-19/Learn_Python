s = set() # no repetition allowed!
s.add(1)
s.add(2) # or set ={1,2}  sets are unordered and dpesnt have index values and immutable only lists and dict are mutable
#sets are like dict but cant have duplicate entries 

# Original set
s = {1, 8, 2, 3}
print("Original set:", s)

# 1. len(): Get number of elements in set
print("\n1. len(s):", len(s))  # Output: 4

# 2. remove(): Remove a specific element
s.remove(8)
print("2. After s.remove(8):", s)  # Output: {1, 2, 3}

# 3. pop(): Remove and return an arbitrary element (random element)
removed_item = s.pop()
print("3. s.pop() → Removed:", removed_item)
print("   After pop():", s)

# 4. clear(): Empties the set
s.clear()
print("4. After s.clear():", s)  # Output: set()

# Let's recreate the original set for union and intersection
s = {1, 8, 2, 3}
new_set = {8, 11}

# 5. union(): Combine elements from both sets
union_set = s.union(new_set)
print("\n5. s.union({8, 11}):", union_set)  # Output: {1, 2, 3, 8, 11}

# 6. intersection(): Find common elements
intersection_set = s.intersection(new_set)
print("6. s.intersection({8, 11}):", intersection_set)  # Output: {8}
