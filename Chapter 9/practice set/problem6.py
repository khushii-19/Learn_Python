# Write a program to mine a log file and find out whether it contains ‘python’

with open("Chapter 9/practice set/log.txt") as f:
    content = f.read()
if("Python" in content ):
    print("Yes python is present")
else:
    print("Python is not present")    
