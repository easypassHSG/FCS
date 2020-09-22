#!/usr/bin/env python3




import random

#We create a variable numberOfFlips in order to inform the player how many flips he has performed in the end
numberOfFlips = 0


def startGame():
    """This function starts the coin flip game and repeats coin flips until the player wins or loses"""
    
    #In order to access and change the variables value we need to declare that it is a global variable
    global currentMoney
    
    #The while function prevents the player from playing when he has no money anymore or has reached the cash goal
    while (currentMoney > 0) and (currentMoney < cashGoal):
        
        # With this line we prevent the game to run incidently, we want that the user has to start each coin flip manually
        input("Press Enter to flip the coin...")
        
        
        if random.randrange(0,2) == 0:
            
            currentMoney += 1
            print("You have won!!! Your current money increased by 1 and is now", currentMoney)
        else:
            
            currentMoney -= 1
            print("Unfortunately you lost. You have", currentMoney, "left to play.")
            
        # After each coin flip we increment the numberOfFlips by 1    
        global numberOfFlips
        numberOfFlips += 1
        
    else:
        # As soon the criteria of the while loop is not fulfilled anymore, we know that the player either has lost or won. The if statement check which of these options is the case.
        if currentMoney <= 0:
            print("You lost all your money after", numberOfFlips, "coin flips. Please restart the game if you want to play again.")
        elif currentMoney >= cashGoal:
            print("Congratulation you won", currentMoney, "CHF after", numberOfFlips, "coin flips.")
        




#Firstly, ask user of the stake, which automatically becomes the currentMoney available to the player
stake = int(input("What is your preferred stake? "))
currentMoney = stake

#Secondly, ask the user of the cash goal he want to reach
cashGoal = int(input("What is your desired cash goal? "))


#We need the cash goal to be bigger than the stake/currentMoney. That's why we keep asking till the cashGoal is higher than the currentMoney (in case the user inputs wrong numbers)
while cashGoal <= currentMoney:
    cashGoal = int(input("Your cash goal needs to be bigger than your current money. Please reenter a higher number! "))



#We call the function startGame() to start the game
startGame()


    
