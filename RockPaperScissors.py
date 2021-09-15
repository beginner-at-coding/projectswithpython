from random import randint #do not use colons, paranthesis or any arguments

#Creating the list for python operators
t=["Rock", "Paper", "Scissors", "Exit!"]

#assigning a random play for the computer.
computer=t[randint(0,2)] 

#Setting the player value to false
player=False

while player==False:
    #Set the player value to True
    player=input("Pick your side and type - Rock, Paper, Scissors - ")
    if player==computer:
        print("Tie!")
        player=False
    elif player=="Rock":
        if computer=="Paper":
            print("You Lose!", computer, "covers", player )
            player=False
    
        else:
            print("You win", player, "smashes", computer)
            
            player=False
    
    elif player=="Paper":
        if computer=="Scissors":
            print("You Lose!", computer, "cut", player )
            player=False
    
        else:
            print("You win", player, "covers", computer)
            player=False
    

    elif player=="Scissors":
        if computer=="Rock":
            print("You Lose!", computer, "smashes", player )
            player=False
    
        else:
            print("You win", player, "cut", computer)
            player=False
    
    elif player=="Exit!":
        player=True
        print("Exiting the Game")

    else:
        print("Invalid Player, Try Again!")
        player=False

    
    computer=t[randint(0,2)]
player==False