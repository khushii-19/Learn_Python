# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

spam = input("Enter any prompt or text: ").lower()

if ("make a lot of money" in spam or
    "buy now" in spam or
    "subscribe this" in spam or
    "click this" in spam):
    print(" This is a spam comment!")
else:
    print(" This is not spam.")

# using in with strings