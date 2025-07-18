# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

with open("Chapter 9/practice set/poems.txt") as f:
    content= f.read()
    if("twinkle" in content ):
        print("word found")
    else:
        print("twinkle is missing")    