# this is rock paper and scissor will continue till i want

import random

print("🎮 Welcome to Rock Paper Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'exit' to quit the game.\n")

while True:
    user = input("Your choice: ").lower()  # user input in lowercase

    if user == "exit":
        print("Thanks for playing! 👋")
        break

    if user not in ["rock", "paper", "scissors"]:
        print("❌ Invalid input! Please choose rock, paper, or scissors.\n")
        continue

    computer = random.choice(["rock", "paper", "scissors"])  # computer move

    print(f"Computer chose: {computer}")

    # ✅ Check draw
    if user == computer:
        print("It's a draw!\n")

    # ✅ Winning conditions for user
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        print("🎉 You win!\n")

    # ✅ Otherwise, computer wins
    else:
        print("💻 Computer wins!\n")
