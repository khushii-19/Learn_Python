# We are going to write a program that generates a random number and asks the user to
# guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower
# number please”. Similarly, if the user’s guess is too low, the program prints “higher
# number please” When the user guesses the correct number, the program displays the
# number of guesses the player used to arrive at the number.


import random

n = random.randint(1,100)
print("Hey we are playing the guessing game and you have to guess the number between 1 - 100 in minimum number of guesses")
a = 0
guesses = 0
while (a!=n):
    a = int(input("Guess the number: "))
    if a == n:
        if guesses == 0:
            print(f"Amazing!  You guessed the number {n} correctly on the **first try**!")
        else:
            print(f"Well done! You guessed the number {n} in {guesses + 1} trials.")
        break
    elif a < n:
        print("Guess a higher number")
    elif a > n:
        print("Guess a lower number")
    guesses += 1



