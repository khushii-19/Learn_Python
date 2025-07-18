# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random
def game():
    print("You are playing a game...")
    score = random.randint(1,70)   #its a game returning random integer using random.randint between range (1-69)
 
 #fetching hiscore
    with open("Chapter 9/practice set/hiscore.txt") as f:
        hiscore = f.read()   #now it reads in string format whatever in file as int ot reads that in str
        if(hiscore == ""):
            hiscore = 0   #use int mae 0 manna hoga empty file h to
        else:
            hiscore = int(hiscore)  #mtlb jo bhi hiscore ki value h vo sting mae read hogi to use int mae convert krlia jisse aage compare kr sake

    print(f"Your score : {score}")
    if(score>hiscore):    #first check whether score>hiscore then only write othwerwise whether your score is not greater it will erase because noothing is given in else    to agar score bada h to he file open kro
        with open("Chapter 9/practice set/hiscore.txt", "w") as f:
          f.write(str(score))   #now ab write krna h to str mae hoga write
    return score              

game()

