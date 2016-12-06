import random
MAXSIZE = 10
grid = []
for row in range(MAXSIZE):
    line=[]
    for col in range(MAXSIZE):
        x=random.randint(1,100)
        if x <=10:
            line.append("G")
        elif x>10 and x <=20:
            line.append("U")
        elif x>20 and x<=30:
            line.append("S")
        else:
            line.append("*")
    grid.append(line)
for row in range(len(grid)):
   for col in range(len(grid[row])):
       print (grid[row][col], end='')
   print()