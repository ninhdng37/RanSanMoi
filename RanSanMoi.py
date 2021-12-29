#   SNAKE GAME
#   Author : Apaar Gupta (@apaar97)
#   Python 3.5.2 Pygame
#
import pygame
import sys
import time
import random
import tkinter as tk
from tkinter import messagebox

# Pygame Init
init_status = pygame.init()
if init_status[1] > 0:
    print("(!) Had {0} initialising errors, exiting... ".format(init_status[1]))
    sys.exit()
else:
    print("(+) Pygame initialised successfully ")

# Play Surface
size = width, height = 320, 320
playSurface = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")

# Colors
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 42, 42)

# FPS controller
fpsController = pygame.time.Clock()

# Game settings
delta = 10
snakePos = [100, 150]
snakeBody = [[100, 150], [90, 150],[80,150]]
foodPos = [0, 0]
foodSpawn = False
direction = 'RIGHT'
changeto = ''
score = 0
def drawGrid(w, rows, surface):
    #sizeBtwn = w // rows
    x = 0
    y = 20
    for l in range(w):
        x = x + rows
        # y = y + rows
        pygame.draw.line(surface, (0,0,0), (x,30),(x,w))
        # pygame.draw.line(surface, (0,0,0), (0,y),(w,y))
    for l in range(30,w):
        y += rows
        pygame.draw.line(surface, (0,0,0), (0,y),(w,y))
def randomSnack(rows, item):
    # positions = item
    l = list()
    l1 = list()
    # l2 = list()
    # l = [[i for i in range(0,rows,10)],[j for j in range(0,rows,10)]]
    for i in range(0, rows, 10):
        for j in range(30, rows, 10): 
            l.append([i,j])
    # l1 = list(set(l) ^ set(item))
    l1 = [x for x in l if x not in item]
    # while True:
    #     x = random.randrange(len(l))
    #     y = random.randrange(len(l))
    #     if len(list(filter(lambda z:z == [l[x],l[y]], positions))) > 0:
    #         continue
    #     else:
    #         break
    # x = random.randrange(len(l))
    # y = random.randrange(len(l))
    return l1[random.randrange(len(l1))]
def reset():
    global delta, snakePos, snakeBody, foodSpawn, direction, changeto, score
    snakePos = [100, 150]
    snakeBody = [[100, 150], [90, 250],[80,150]]
    foodPos = [0, 0]
    foodSpawn = False
    direction = 'RIGHT'
    changeto = ''
    score = 0
    pygame.display.update()
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], delta, delta))
    foodPos = randomSnack(height, snakeBody)
    #foodPos = [random.randrange(1, width // 10) * delta, random.randrange(1, height // 10) * delta]
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta))
# Game Over
def gameOver():
    global score, direction
    # myFont = pygame.font.SysFont('monaco', 72)
    # GOsurf = myFont.render("Game Over", True, red)
    # GOrect = GOsurf.get_rect()
    # GOrect.midtop = (320, 25)
    # playSurface.blit(GOsurf, GOrect)
    # showScore(0)
    direction = 'RIGHT'
    pygame.display.flip()
    # time.sleep(4)
    # reset()
    # root = tk.Tk()
    # root.attributes("-topmost", True)
    # root.withdraw()
    # messagebox.showinfo('You Lost!', 'Play again...')
    # reset()
    score = 0
    #pygame.quit()
    #sys.exit()

# Show Score
def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
def showScore(choice=1):
    SFont = pygame.font.SysFont('monaco', 32)
    Ssurf = SFont.render("Score  :  {0}".format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (320, 100)
    playSurface.blit(Ssurf, Srect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Validate direction
    if changeto == 'RIGHT' and direction != 'LEFT':
        direction = changeto
    if changeto == 'LEFT' and direction != 'RIGHT':
        direction = changeto
    if changeto == 'UP' and direction != 'DOWN':
        direction = changeto
    if changeto == 'DOWN' and direction != 'UP':
        direction = changeto

    # Update snake position
    if direction == 'RIGHT':
        snakePos[0] += delta
    if direction == 'LEFT':
        snakePos[0] -= delta
    if direction == 'DOWN':
        snakePos[1] += delta
    if direction == 'UP':
        snakePos[1] -= delta

    # Bounds
    if snakePos[0] >= width: snakePos[0] = 0
    elif snakePos[0] < 0: snakePos[0] = width
    elif snakePos[1] >= height: snakePos[1] = 30
    elif snakePos[1] < 30: snakePos[1] = height          
    # Snake body mechanism
    snakeBody.insert(0, list(snakePos))
    if snakePos == foodPos:
        foodSpawn = False
        score += 1
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = randomSnack(height, snakeBody)
        #foodPos = [random.randrange(1, width // 10) * delta, random.randrange(1, height // 10) * delta]
        foodSpawn = True

    playSurface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], delta, delta))
    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], delta, delta)) 
    # if snakePos[1] >= height or snakePos[1] < 0:
    #    for pos in snakeBody:
    #      pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], delta, delta))      
         
    # Self hit
    for block in snakeBody[1:]:
        if snakePos == block:
            gameOver()
            message_box('You Lost!', 'Game over...\nPlay again')
            reset()
    showScore()
    drawGrid(height,delta,playSurface)
    pygame.display.flip()
    fpsController.tick(10)