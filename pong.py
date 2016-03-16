import time
from os import system
from sys import argv, exit

# Cannot run without at least a grid size
if len(argv) < 3:
    print "Usage:"
    print "python pong.py gridx gridy [deltax] [deltay]"
    exit()

x = int(argv[1])
y = int(argv[2])

# If user gives the delta for the x and y, set them to those, otherwise set each to 1
if len(argv) == 5:
    dx = int(argv[3])
    dy = int(argv[4])
else:
    dx = 1
    dy = 1

# Returns a new grid that is x by y characters
def clearGrid(x, y):
    return [[" " for num in range(x)] for num in range(y)]

# initialize the grid
grid = clearGrid(x, y)

class ball():
    # Every ball needs a position, a bounding box, and a velocity
    def __init__(self, x, y, gridx, gridy, dx, dy):
        self.x = x
        self.y = y
        self.gridx = gridx
        self.gridy = gridy
        self.dx = dx
        self.dy = dy
        self.tempRow = ""

    # Reverses the velocity of the ball
    def reflectx(self):
        self.dx *= -1

    def reflecty(self):
        self.dy *= -1

    # Movement logic. Updates position, then checks to see if ball is in bounds
    # If ball is out of bounds, move ball in bounds and reflect that velocity
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

    # Updates the position of the ball with self.update(), then draws the grid

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

        # On-screen reporting of ball position
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

# Initialize ball
b = ball(1, 1, x, y, dx, dy)

try:
    while True:
        b.draw(grid)
        time.sleep(0.1)
# Because I'm an idiot, catch any errors that result from being out of bounds,
# then log the position and velocity of the ball as well as the entire grid 
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
# Close the program if the user performs a keyboard interrupt
except(KeyboardInterrupt):
    print "\nGood bye\n"
    time.sleep(1)
    system("clear")
    exit()
