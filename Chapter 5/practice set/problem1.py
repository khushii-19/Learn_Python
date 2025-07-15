# # Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

my_dict = {
    "madad":"help",
    "bech do":"sell",
    "bura" : "bad",
    "billi" : "cat"
}
print(my_dict)
answer = input("Enter word to find from dictionary").strip()
print(my_dict.get(answer))
