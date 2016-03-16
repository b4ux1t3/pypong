import time
from os import system
from sys import argv, exit

if len(argv) < 3:
    print "Usage:"
    print "python pong.py gridx gridy [deltax] [deltay]"
    exit()

x = int(argv[1])
y = int(argv[2])

if len(argv) == 5:
    dx = int(argv[3])
    dy = int(argv[4])
else:
    dx = 1
    dy = 1

def clearGrid(x, y):
    return [[" " for num in range(x)] for num in range(y)]

grid = clearGrid(x, y)

class ball():

    def __init__(self, x, y, gridx, gridy, dx, dy):
        self.x = x
        self.y = y
        self.gridx = gridx
        self.gridy = gridy
        self.dx = dx
        self.dy = dy
        self.tempRow = ""


    def reflectx(self):
        self.dx *= -1

    def reflecty(self):
        self.dy *= -1

    def update(self):
        self.x += self.dx
        self.y += self.dy

        if self.y >= self.gridy - 1:
            self.y = self.gridy - 1
            self.reflecty()
        elif self.y <= 0:
            self.y = 0
            self.reflecty()

        if self.x >= self.gridx - 1:
            self.x = self.gridx - 1
            self.reflectx()
        elif self.x <= 0:
            self.x = 0
            self.reflectx()

    def draw(self, grid):
        system("clear")
        grid = clearGrid(self.gridx, self.gridy)
        self.update()
        grid[self.y][self.x] = "*"
        for i in grid:
            for j in i:
                self.tempRow += j
            print self.tempRow
            self.tempRow = ""
        if self.x < 10:
            stringSelfX = "00" + str(self.x)
        elif self.x < 100:
            stringSelfX = "0"+ str(self.x)

        if self.y < 10:
            stringSelfY = "00" + str(self.y)
        elif self.x < 100:
            stringSelfY = "0"+ str(self.y)


        print "x: " + stringSelfX + " | dx: " + str(self.dx)
        print "y: " + stringSelfY + " | dy: " + str(self.dy)


b = ball(1, 1, x, y, dx, dy)
try:
    while True:
        b.draw(grid)
        time.sleep(0.1)
except(IndexError):
    tempRow = ""
    f = open("log.txt", "w")
    f.write("x: " + str(b.x) + " | dx: " + str(b.dx) + "\n")
    f.write("y: " + str(b.y) + " | dy: " + str(b.dy) + "\n")
    for i in grid:
        for j in i:
            tempRow += j
        f.write(tempRow + "\n")
        tempRow = ""
    f.close()
except(KeyboardInterrupt):
    print "\nGood bye\n"
    time.sleep(1)
    system("clear")
    exit()
