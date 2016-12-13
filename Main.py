# Treasure World Game

import random
win = True
gold = 0
lives = 3
turnsOfOmnisense = 0
Censor = True
xLocation = 0
yLocation = 0
random_or_not = 0

def load_grid():
    Grid = []
    with open("scratch_1.txt", "r") as file:      # Opens file as file
        Data_from_txt_file = file.readlines()# Read the lines and store it.
    for lines in Data_from_txt_file:         # for every line in the file
        lines = lines.strip("\n")            # Discard \n from the lines
        list_of_lines = list(lines)          # Separates each character in each line
        Grid.append(list_of_lines)           # Put every list into another list
        file.close()
    return Grid


def event(world,x,y,gold,lives,censor):
    if world[x][y] == "G":
        gold += 1
    elif world[x][y] == "S":
        lives -=1
    elif world[x][y] == "U":
        censor += 3
    return gold,lives,censor


def Random_grid(height, length):
    Grid = []
    for row in range(length):                # loop length amount of times
        Line = []
        for column in range(height):         # loop height amount of times
            x = random.randint(1, 100)       # x is random number from 0 to 100
            if x<=10:                        # if x is less than 11
                Line.append("G")             # Write 'G' in line
            elif x>=11 and x<=15:            # if x is more than 10 and less than 16
                Line.append("U")             # Write 'U' in line
            elif x>=16 and x<=26:            # if x is more than 15 and less than 26
                Line.append("S")             # Write 'S' in line
            else:
                Line.append("~")             # Otherwise write '~'
        Grid.append(Line)                    # Append each line into grid
    return Grid

def reveal_grid(Grid, censor):
    for x in range(len(Grid)):               # len(Grid) counts amount of items in Grid and x is from zero to amount og items in grid
        for y in range(len(Grid)):
            if censor:                       # If censor is true
                print("~", end = "")         # All should be '~'
            else:
                print(Grid[x][y], end = "")  # Otherwise print the actual Grid
        print()                              # moves every list in list into another line

def PlayerLocation(Grid,xlocation,ylocation):
    Grid[xlocation][ylocation] = "#"
    return Grid



try:
    random_or_not = int(input("Load grid from txt file (Enter 1)\n"
                        "and a randomly generated grid (enter 2)\n"
                        "> "))
except:
    print("Wrong input. Please enter again.\n")



if random_or_not == 1:
    world = load_grid()
    world = PlayerLocation(world,xLocation,yLocation)
    reveal_grid(world, True)
    print()



elif random_or_not == 2:
    world = Random_grid(10, 10)                # Randomly generates a 10x10 grid
    reveal_grid(world, True)                 # Prints the grid censored
    print()


while lives > 0:
    world = PlayerLocation(world,xLocation,yLocation)
    print("The player is at",xLocation,",",yLocation,)
    movement=input("Which way do you want to go?\n> ").lower()
    if movement == "w":
        world[xLocation][yLocation]="*"
        xLocation -= 1
        if xLocation < 0:
            xLocation +=1
    elif movement == "s":
        world[xLocation][yLocation] = "*"
        xLocation += 1
        if xLocation >= 10:
            xLocation -=1
    elif movement == "d":
        world[xLocation][yLocation] = "*"
        yLocation += 1
        if yLocation >= 10:
            yLocation -=1
    elif movement == "a":
        world[xLocation][yLocation] = "*"
        yLocation -= 1
        if yLocation < 0:
            yLocation +=1
    elif movement == "stats()":
            print("Gold:",gold,"\nLives:",lives,"\nTurns of Omnisense left:",turnsOfOmnisense)
    elif movement == "debug()":
            turnsOfOmnisense+=3
    else:
        print("Wrong input! Try again")

    gold,lives,turnsOfOmnisense=event(world,xLocation,yLocation,gold,lives,turnsOfOmnisense)
    world= PlayerLocation(world,xLocation,yLocation)
    if turnsOfOmnisense > 0:
        Censor = False
        turnsOfOmnisense-=1
    print()
    reveal_grid(world, Censor)
    print()
    if turnsOfOmnisense == 0:
        Censor = True
    if gold == 3:
        break


if lives == 0:
    win = False
if win:
    print("You win")
else:
    print("You lose")