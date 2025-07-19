# Write a program to make a copy of a text file “this. txt”

with open("Chapter 9/practice set/this.txt")as f:
    copy = f.read()
with open("Chapter 9/practice set/copy.txt","w")as f:
    copied = f.write(copy)   #write creates a new file if not exist


# Write a program to find out whether a file is identical & matches the content of
# another file.    

if(copied==copy):
    print("content is matched")   # this cant be done because it has written there it cant be stored in a vairable for that you have to read both files now 

with open("Chapter 9/practice set/copy.txt","r")as f:
    contentnew = f.read()
if(copy==contentnew):
    print("content is matched")    #agar ye baad mae likho to content to delete ho chuka matcghed ni aayega isliye pahle likhna hoga


# Write a program to wipe out the content of a file using python    

with open("Chapter 9/practice set/copy.txt","w")as f:
    f.write("")


