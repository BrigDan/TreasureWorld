import random


def loadGridFromFile():
    grid = []
    with open("world1.txt") as f:
        fileContents = f.readlines()

    for line in fileContents:
        line = line.strip('\n')
        l = list(line)
        grid.append(l)

    return grid


def showGrid(grid, censor):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if censor:
                print('*', end='')
            else:
                print(grid[x][y], end='')
        print()


def createRandomGrid(size):
    grid = []
    # build the contents here
    for row in range(size):
        line = []
        for col in range(size):
            # get a random number betwen 1-100
            x = random.randint(1, 100)
            if x <= 10:
                line.append('G')
            elif x > 10 and x <= 15:
                line.append('U')
            elif x > 15 and x <= 25:
                line.append('S')
            else:
                line.append('*')

        grid.append(line)

    return grid


def placePlayerInWorld(grid, size):
    # bottom left
    grid[size][0] = '#'
    # top right
    grid[0][size] = '#'
    # random position - wipes out whatever was there
    grid[random.randint(0, size)][random.randint(0, size)]
    # first check if the space is empty '*' and keep finding new
    # random positions until an empty space is found


    return grid


# main program starts here
world = createRandomGrid(10)
world = placePlayerInWorld(world, 10)
showGrid(world, True)
print()
showGrid(world, False)


