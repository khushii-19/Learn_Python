a = {
"key": "value",
"harry": "code",
"marks": "100",
"list": [1, 2, 9]
}
print(a["key"]) # Output: "value"
print(a["list"]) # Output: [1, 2, 9]

# Sample dictionary
a = {
    "name": "harry",
    "from": "india",
    "marks": [92, 98, 96]
}

# 1. a.items(): Returns all (key, value) pairs as tuples
print("a.items():", a.items())
# Output: dict_items([('name', 'harry'), ('from', 'india'), ('marks', [92, 98, 96])])

# 2. a.keys(): Returns all keys in the dictionary
print("a.keys():", a.keys())
# Output: dict_keys(['name', 'from', 'marks'])

# 3. a.update({"friends": ["ron", "hermione"]}): Adds or updates a key-value pair
a.update({"friends": ["ron", "hermione"]})
print("After update:", a)
# Output includes new key 'friends': {'name': 'harry', ..., 'friends': ['ron', 'hermione']}

# 4. a.get("name"): Returns the value for the key "name"
print('a.get("name"):', a.get("name"))
# Output: harry


print("Original dictionary:", a)

# values(): Get all values
print("\n1. a.values():", a.values())

# pop(): Remove 'from' key
removed = a.pop("from")
print("2. a.pop('from') → Removed value:", removed)
print("   After pop():", a)

# popitem(): Remove last inserted item
last_item = a.popitem()
print("3. a.popitem() → Removed:", last_item)
print("   After popitem():", a)

# clear(): Remove all items
a.clear()
print("4. a.clear() → Dictionary after clearing:", a)

# copy(): Copy a dictionary
a = {"x": 1, "y": 2}
b = a.copy()
print("\n5. a.copy() → Copy of dictionary:", b)

# setdefault(): Return or set default value
val = a.setdefault("z", 10)
print("6. a.setdefault('z', 10) → Value:", val)
print("   Dictionary after setdefault():", a)

# dict.fromkeys(): Create new dictionary from keys
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("\n7. dict.fromkeys(['a', 'b', 'c'], 0) →", new_dict)


