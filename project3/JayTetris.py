# Tetris Game
# Jay Becker IT3038C Project 3
# Coded following TokyoEdtech tutorial on YouTube (https://www.youtube.com/watch?v=JuMqaU_664k)
# Uses Python 3 & Turtle Module

import turtle
import time
import random

# window setup
wn = turtle.Screen()
wn.title("Tetris Game - Project 3 - Jay Becker")
wn.bgcolor("black")
wn.setup(width=350, height=600)
wn.tracer(0)

delay = 0.15

# shape generation
class Shape():
    # initialization
    def __init__(self):
        self.x = 5
        self.y = 0
        self.color = random.randint(1, 12)


        # define shape options
        square = [[1,1],
                  [1,1]]

        horz_line = [[1,1,1,1]]

        vert_line = [[1],
                         [1],
                         [1],
                         [1]]

        l_left = [[1,0,0,0],
                  [1,1,1,1]]
                   
        l_right = [[0,0,0,1],
                   [1,1,1,1]]
                   
        s_left = [[1,1,0],
                  [0,1,1]]
                  
        s_right = [[0,1,1],
                   [1,1,0]]
                  
        t = [[0,1,0],
             [1,1,1]]

        # array of shapes
        shapes = [square, horz_line, vert_line, l_left, l_right, s_left, s_right, t]

        # randomly choose shape
        self.shape = random.choice(shapes)             
        self.height = len(self.shape)
        self.width = len(self.shape[0])
    
    # shape actions
    def shift_left(self, grid):
        if self.x > 0:
            if grid[self.y][self.x - 1] == 0:
                self.destroy_shape(grid)
                self.x -= 1
        
    def shift_right(self, grid):
        if self.x < 12 - self.width:
            if grid[self.y][self.x + self.width] == 0:
                self.destroy_shape(grid)
                self.x += 1
    
    def create_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = self.color
                
    def destroy_shape(self, grid):
        for y in range(self.height):
            for x in range(self.width):
                if(self.shape[y][x]==1):
                    grid[self.y + y][self.x + x] = 0
                    
    def movable(self, grid):
        result = True
        for x in range(self.width):
            if(self.shape[self.height-1][x] == 1):
                if(grid[self.y + self.height][self.x + x] != 0):
                    result = False
        return result
    
    def spin(self, grid):
        self.destroy_shape(grid)
        updated_shape = []
        for x in range(len(self.shape[0])):
            updated_row = []
            for y in range(len(self.shape)-1, -1, -1):
                updated_row.append(self.shape[y][x])
            updated_shape.append(updated_row)
        
        right_side = self.x + len(updated_shape[0])
        if right_side < len(grid[0]):
            self.shape = updated_shape
            self.height = len(self.shape)
            self.width = len(self.shape[0])

# create game grid         
grid = [
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13],
    [13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13]
]

# initialize pen
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.shape("circle")
pen.setundobuffer(None)

def generate_grid(pen, grid):
    pen.clear()
    top = 230
    left = -110
    
    colors = ["black", "cyan", "dodgerblue", "darkorange", "yellow", "lawngreen", "darkviolet", "firebrick", "springgreen", "hotpink", "coral", "chocolate", "steelblue", "white"]
    
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            xcoord = (left + (x * 22)) - 27
            ycoord = top - (y * 22) + 10
            color_ID = grid[y][x]
            color = colors[color_ID]
            pen.color(color)
            pen.goto(xcoord, ycoord)
            pen.stamp()


def check_rows(grid):
    # check for full row events
    y = 23
    while y > 0:
        full = True


        for x in range(0, 12):

            if grid[y][x] == 0:
                full = False
                y -= 1

                break

        if full:

            global score
            score += 100
            update_scoreboard(pen, score)

            for copy_y in range(y, 0, -1):
                for copy_x in range(0, 12):
                    grid[copy_y][copy_x] = grid[copy_y-1][copy_x]

def update_scoreboard(pen, score):
    pen.color("white")
    pen.hideturtle()
    pen.goto(0, 240)
    pen.write("Score: {}".format(score), move=False, align="center", font=("Impact", 30, "normal"))
    

# initialize shape
shape = Shape()

# drop shape onto grid
grid[shape.y][shape.x] = shape.color


# listen for movement instructions
wn.listen()
wn.onkeypress(lambda: shape.shift_left(grid), "Left")
wn.onkeypress(lambda: shape.shift_right(grid), "Right")
wn.onkeypress(lambda: shape.spin(grid), "space")

score = 0

update_scoreboard(pen, score)

# game loop
while True:
    wn.update()
    if shape.y == 23 - shape.height + 1:
        shape = Shape()
        check_rows(grid)

    elif shape.movable(grid):
        shape.destroy_shape(grid)
        shape.y +=1
        shape.create_shape(grid)

    else:
        shape = Shape()
        check_rows(grid)

    generate_grid(pen, grid)
    update_scoreboard(pen, score)
    
    time.sleep(delay)
    
wn.mainloop()