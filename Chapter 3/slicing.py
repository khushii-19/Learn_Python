#slicing starts from 0 and to last digit but last digit is not counted
# s[start:end:skip]

a = "khushi"
s1 = a[1:3] # returns hu only 
print (s1)

# negative indices and slicing can also be done and it can be only done ffrom left to right
s2 = a[-5:-1] #returns hush
print (s2)

# SLICING WITH SKIP VALUE
word = "amazing"
s3 = word[1: 6: 2] # "mzn"
# Other advanced slicing techniques:

s4 = word[:7] # word [0:7] – 'amazing'
s5=  word[0:] # word [0:7] – 'amazing
print(s3)
print(s4)
print(s5)