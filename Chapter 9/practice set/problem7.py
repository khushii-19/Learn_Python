# Write a program to find out the line number where python is present from ques 6.

# Write a program to mine a log file and find out whether it contains ‘python’

with open("Chapter 9/practice set/log.txt") as f:
    content = f.readlines()  #list mae store krlia and ab list k ek ek element ko iterate kia i mean ek eke line ko
line_no = 1  # to get line number we initialise line no = 1
for l in content:
  if("Python" in l ):
    print("Yes python is present at line no : ", line_no)
    break
  line_no += 1 #jisse vo next line pe jaye  
else:
    print("Python is not present")    #this should be out of for loop only because loop cmplete hogya tab ye print ho pahle nhi
  


