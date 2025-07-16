import random
# snake = 0
# water = 1
# gun = -1 

computer = random.choice([0,1,-1])
youstr = input("Enter your choice : s,w,g : ")
you_dict = {"s":0, "w":1, "g":-1}
reverse_dict = {0:"snake", 1:"water",-1:"gun"}
you = you_dict[youstr]

print(f"You chose {reverse_dict[you]} \n Computer chose {reverse_dict[computer]}")

if(computer==you):
    print("It's a draw")

else:
    if(computer == 0 and you == 1):
        print("You lose")
    elif(computer == 1 and you == 0):
        print("You win")
    elif(computer == 1 and you == -1):
        print("You lose")    
    elif(computer == 0 and you == -1):
        print("You win")
    elif(computer == -1 and you == 0):
        print("You lose") 
    elif(computer == -1 and you == 1):
        print("You win")           
    else:
        print("Something went wrong")    