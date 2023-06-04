#   1. Import pygame and random and initialize the game
#   2. Define constants and cell size, rows, colums, colors
#   3. Create Tetris game board and grid lines
#   4. Define Shapes create functions that will handle rotation and draw the shapes into grid
#   5. Functions that will happen after player inputs
#   6. Clock to control game speed
#   7. Collisions
#   8. Something to detect lose also when row is full
#   9. Score to keep track of points
#   10.Player inputs
#


import pygame
import random


pygame.init()

# constants
height = 601
width = 500
title = "tetris"
game_height = 600
game_width = 300

#cell size
cell= 30

rows = (height - game_height) // 2
cols = (width - game_width)

#screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)

 # colors ( red, green, blue)


running = True



# def fill_board(pos={}):
#     board = [[0,0,0] for _ in  range(10) for _ in range(20)]
#     for i in range(board):
#         for j in range(len(board[i])):
#             if(j,i) in pos:
#                 temp = pos[(j,i)]
#                 board[i][j] = temp
#     return board

        

l = [['0...',
      '0...',
      '00..',
      '....'],
     ['....',
      '000.',
      '0...',
      '....'],
     ['00..',
      '.0..',
      '.0..',
      '....'],
     ['..0.',
      '000.',
      '....',
      '....']]  

i = [['0...',
      '0...',
      '0...',
      '0...'],
     ['....',
      '0000',
      '....',
      '....']]

r = [['00..',
      '0...',
      '0...',
      '....'],
     ['0...',
      '000.',
      '....',
      '....'],
     ['.0..',
      '.0..',
      '00..',
      '....'],
     ['....',
      '000.',
      '..0.',
      '....']]

o = [['00..',
      '00..',
      '....',
      '....']]

s = [['.00.',
      '00..',
      '....',
      '....'],
     ['0...',
      '00..',
      '.0..',
      '....']]

t = [['000.',
      '.0..',
      '....',
      '....'],
     ['.0.',
      '00..',
      '.0..',
      '....'],
     ['.0..',
      '000.',
      '....',
      '....'],
     ['.0..',
      '.00.',
      '.0..',
      '....']]
z = [['00..',
      '.00.',
      '....',
      '....'],
     ['.0..',
      '00..',
      '0...',
      '....']]
white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0,255, 255)
blue = (0, 0, 255)
orange = (255,160, 0)
yellow = (255,255, 0)
green = (0,255, 0)
purple = (160,32, 240)
red = (255,0, 0)

shapes = [l,i,r,o,s,t,z]
colors = [cyan, blue,orange,yellow, green,purple,red]

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0
        
def draw_window(screen, grid, score = 0, lastscore = 0):
        screen.fill(black)
        pygame.font.init()
        font = pygame.font.SysFont('Arial',60)
        label = font.render("Tetris", 1, white)
        draw_grid(screen, grid)
        
        
def draw_grid(screen, grid):
    x = game_width // cell + 1
    y = game_height // cell + 1
    for i in range(len(grid)):
        pygame.draw.line(screen, white, (i * cell, 0), (i * cell, game_height))
        for j in range(len(grid[i])):
            pygame.draw.line(screen, white, (0, j * cell), (game_width, j * cell))

def create_grid(locked_pos={}):
    grid = [[(0,0,0) for i in range(10)] for j in range(20)]
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(j,i) in locked_pos:
                c = locked_pos[(j,i)]
                grid[i][j] = c
    return grid

def if_valid(shape, grid):
    vaild_pos = [[(j,i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
    vaild_pos = [j for sub in vaild_pos for j in sub]
    
    format = convert_shapes(shape)
    
    for pos in format:
        if pos not in vaild_pos:
            if pos[1]> -1:
                return False
    return True;   
 
def convert_shapes(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    
    for i, line in enumerate(format):
        row = list(line)
        for j, col in enumerate(row):
            if col == '0':
                positions.append((shape.x + j, shape.y + i))
    for i, pos in enumerate(positions):
        positions[i] = (pos[0], pos[1])   
    return positions
        

def get_shape():
    return Piece(5, 0, random.choice(shapes))      
        
        
def main():
    screen = pygame.display.set_mode((width, height))
    locked_positions = {}
    grid = create_grid(locked_positions)
    current = get_shape()
    change = False
    next = get_shape()
    fall_speed = 0.5
    score = 0
    while(True):
        grid = create_grid(locked_positions)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                running = False
        
        
        current.y+=1
        if not(if_valid(current, grid)) and current.y > 0:
            current.y -= 1
            change = True
        draw_window(screen, grid,score,score)     
        pygame.display.update()
        
main()
        



