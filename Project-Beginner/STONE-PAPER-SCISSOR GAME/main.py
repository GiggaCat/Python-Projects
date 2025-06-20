#Making a rock, paper and scissor game.
'''
rock = 1
paper = 0
scissor = -1
'''
import random                                          #Random module used to generate random given numbers.

computer = random.choice([1,0,-1])                     #Generate random number between 1,0,-1.
dict1 = {1:"Rock" , 0:"Paper" , -1:"Scissor"}   
print(dict1)
player = int(input("Enter your choice: "))             #User choice
print(f"YOUR CHOICE {dict1[player]}")           
print(f"COMPUTER's CHOICE {dict1[computer]}")

#Conditions to find out weather you win or lose.
if (computer==player):
    print("IT's A DRAW!!!")
else:
    if (computer==1 and player==0):
        print("CONGRATULATION's,YOUR WIN!!!")
    elif (computer==1 and player==-1):
        print("SORRY,YOU LOSE!!!")
    elif (computer==0 and player==1):
        print("SORRY,YOU LOSE!!!")
    elif (computer==0 and player==-1): 
        print("CONGRATULATION's,YOUR WIN!!!")
    elif (computer==-1 and player==1): 
        print("CONGRATULATION's,YOUR WIN!!!")
    elif (computer==-1 and player==0):
        print("SORRY,YOU LOSE!!!")
    else:
        print("INVALID!\nSOMETHING WENT WRONG")