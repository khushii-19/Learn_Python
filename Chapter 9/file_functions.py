f = open("Chapter 9/file.txt")

# lines = f.readlines()
# print(lines, type(lines))    to read lines ek saath saari returns all lines in a list

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# line5 = f.readline()
# print(line5 =="")
line = f.readline()   #read only first line
while(line != ""):
    print(line)
    line = f.readline()
    # Yeh line dubara agli line read karta hai.

    # Agar aap is line ko na likho, toh loop ek hi line pe atak jayega (infinite loop ban jaayega).

    # Isliye, ye line bahut important hai kyunki ye next line fetch karti hai and loop ko aage badhati hai.



f.close()

# append
st = "Hey Khushi you are amazing"

f = open("Chapter 9/myfile.txt", "a")

f.write(st)

f.close()

