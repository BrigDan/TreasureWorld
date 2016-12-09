# Treasure World Game

import random

def load_grid():
    Grid = []
    with open("grid.txt", "r") as file:      # Opens file as file
        Data_from_txt_file = file.readlines()# Read the lines and store it.
    for lines in Data_from_txt_file:         # for every line in the file
        lines = lines.strip("\n")            # Discard \n from the lines
        list_of_lines = list(lines)          # Separates each character in each line
        Grid.append(list_of_lines)           # Put every list into another list
    return Grid

print(load_grid())

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
            if censor:                       # If sensor is true
                print("~", end = "")         # All should be '~'
            else:
                print(Grid[x][y], end = "")  # Otherwise print the actual Grid
        print()                              # moves every list in list into another line

def PlayerLocation(Grid):
    xLocation = 0
    yLocation = 0
    Grid[xLocation][yLocation] = "#"
    return Grid, xLocation, yLocation

random_or_not = int(input("Load grid from txt file (Enter 1)\n"
                          "and a randomly generated grid (enter 2)\n"
                          "=>"))
lives = 3
if random_or_not == 1:
    world = load_grid()
    world, xLocation, yLocation = PlayerLocation(world)
    reveal_grid(world, True)
    print()
    reveal_grid(world, False)
    while lives > 0:
        #lives -= 1
        movement=input("Which way do you want to go?").lower()
        #RightInput = False
        if movement == "w":
            yLocation = yLocation+1
        elif movement == "s":
            yLocation = yLocation-1
        elif movement == "d":
            xLocation = xLocation+1
        elif movement == "a":
            xLocation = xLocation - 1
        else:
            print("Wrong input! Try again")
        world, xLocation, yLocation = PlayerLocation(world)
        print()
        reveal_grid(world, True)
        print()
        reveal_grid(world, False)
elif random_or_not == 2:
    h = int(input("Enter height of World:"))
    l = int(input("Enter length of World:"))
    world = Random_grid(h, l)                # Randomly generates a 10x10 grid
    reveal_grid(world, True)                 # Prints the grid censored
    print()
    reveal_grid(world, False)                # Prints the grid uncensored
