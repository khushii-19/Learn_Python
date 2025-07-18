# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 

# with open("Chapter 9/practice set/donkey.txt") as f:
#     content = f.read()
# content = content.replace("donkey","####")

# with open("Chapter 9/practice set/donkey.txt", "w") as f:
#     f.write(content)

# Agar case-insensitive (Donkey, DONKEY, dOnKeY) replace karna hai to:

# import re
# content = re.sub(r"donkey", "#####", content, flags=re.IGNORECASE

with open("Chapter 9/practice set/donkey.txt", encoding="utf-8") as f:
    content = f.read()

content = content.replace("donkey", "#####")

with open("Chapter 9/practice set/donkey.txt", "w", encoding="utf-8") as f:
    f.write(content)


# UTF-8 ek universal encoding hai jo almost sab characters handle kar leti hai.


