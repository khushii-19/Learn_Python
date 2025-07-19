# Repeat program 4 for a list of such words to be censored.

l1 = ["donkey", "stupid", "idiot"]
with open("Chapter 9/practice set/donkey.txt", encoding="utf-8") as f:
    content = f.read()
for i in l1: #to iterate each word and check jaha bhi aaye replace kro
    content = content.replace(i, "#"*len(i))

with open("Chapter 9/practice set/donkey.txt", "w", encoding="utf-8") as f:
    f.write(content)

