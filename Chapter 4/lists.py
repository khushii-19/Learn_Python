#  lists are containers to store a set of values of any data type.
l1 = [7,9,"harry"]
l1[0] # 7
l1[1] # 9
l1[0:2] # [7,9] #list slicing 

# Original List
l1 = [1, 8, 7, 2, 21, 15]
print("Original list:", l1)

# 1. sort() - Sorts the list in ascending order
l1.sort()
print("After sort():", l1)  # [1, 2, 7, 8, 15, 21]

# 2. reverse() - Reverses the list
l1.reverse()
print("After reverse():", l1)  # [21, 15, 8, 7, 2, 1]

# 3. append(8) - Adds 8 at the end
l1.append(8)
print("After append(8):", l1)  # [21, 15, 8, 7, 2, 1, 8]

# 4. insert(3, 8) - Inserts 8 at index 3
l1.insert(3, 8)
print("After insert(3, 8):", l1)  # [21, 15, 8, 8, 7, 2, 1, 8]

# 5. pop(2) - Removes and returns the element at index 2
removed_item = l1.pop(2)
print("After pop(2):", l1)
print("Popped item:", removed_item)  # Should print 7

# 6. remove(21) - Removes the first occurrence of 21
l1.remove(21)
print("After remove(21):", l1)
