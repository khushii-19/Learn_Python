f = open("Chapter 9/file.txt")
print(f.read())
f.close()

# The same can be written using with statement like this:
with open("Chapter 9/file.txt") as f:
    print(f.readline())

# You dont have to explicitly close the file

# r+ → Read & write (file must exist)
with open("Chapter 9/file.txt", "r+") as f:
    print("r+:", f.read())  # Read existing
    f.write("\nUpdated with r+ mode")  # Add to it

# w+ → Write & read (file is cleared first)
with open("Chapter 9/sample2.txt", "w+") as f:
    f.write("Writing with w+ mode")
    f.seek(0)   #If you just wrote something into the file, and now you want to read from the beginning, you need to move the pointer back. That’s what f.seek(0) does.
    print("w+:", f.read())  # Read what we just wrote

# a+ → Append & read (file created if not exist)
with open("Chapter 9/sample2.txt", "a+") as f:
    f.write("\nNew line with a+ mode")
    f.seek(0)
    print("a+:", f.read())  # Read full content after appending


# Open file for reading in binary mode
with open("Chapter 9/file.txt", "rb") as f2:
    data = f2.read()
    print("rb (read binary):", data)

# Open file for reading in text mode
with open("Chapter 9/file.txt", "rt") as f3:
    data = f3.read()
    print("rt (read text):", data)


