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
height = 620
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

white = (255, 255, 255)
black = (0, 0, 0)
cyan = (0,255, 255)
blue = (0, 0, 255)
orange = (255,160, 0)
yellow = (255,255, 0)
green = (0,255, 0)
purple = (160,32, 240)
red = (255,0, 0)

running = True



def fill_board(pos={}):
    board = [[0,0,0] for _ in  range(10) for _ in range(20)]
    for i in range(board):
        for j in range(len(board[i])):
            if(j,i) in pos:
                temp = pos[(j,i)]
                board[i][j] = temp
    return board

def draw_grid():
    x = game_width // cell + 1
    y = game_height // cell + 1
    for i in range(x):
        pygame.draw.line(screen, white, (i * cell, 0), (i * cell, game_height))
    for j in range(y):
        pygame.draw.line(screen, white, (0, j * cell), (game_width, j * cell))
        
        
shapes = [
    [(1,0), (1,1), (1,2),(0,2)], # l shape
    [(0,0), (0,1), (0,2),(0,3)], # i shape
    [(0,0), (1,0), (1,1),(1,2)], # r shape
    [(0,0), (0,1), (1,0),(1,1)], # o shape
    [(1,0), (1,1), (0,1),(0,2)], # s shape
    [(1,0), (1,1), (1,2),(0,1)], # t shape
    [(0,0), (0,1), (1,1),(1,2)], # z shape
]

colors= [white, black,cyan, blue,orange,yellow, green,purple,red]


while(running):
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
            
    screen.fill(black)
    draw_grid()
    pygame.display.update()
        
pygame.quit()
        



