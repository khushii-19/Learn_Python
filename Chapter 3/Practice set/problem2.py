# Write a program to fill in a letter template given below with name and date.

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
a = letter.replace("<|Name|>", input("Enter Your Nanme")).replace("<|Date|>", "15th July 2025")
print(a)

# chaininng of replace function
