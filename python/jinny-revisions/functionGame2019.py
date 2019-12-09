# Based on code at:
# http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# 1 - Import pygame library ####################################################
import pygame
from pygame.locals import *
import random

# 2 - Set game global variables ################################################
gridnumbers = int(input("How big do you want the board (width/height)?"))
boardsize = (102*gridnumbers,102*gridnumbers)
screen = pygame.display.set_mode(boardsize)
width, height, margin = 100, 100, 2
BLACK = (0, 0, 0)
WHITE = (255,255,255)
grid = [] # 2D array (list of lists) for board
player = pygame.image.load('../../img/player.jpg').convert()
playerCoord = [0,0]
icon0 = pygame.image.load('../../img/icon0.jpg').convert() 
icon1 = pygame.image.load('../../img/icon1.jpg').convert()
icon2 = pygame.image.load('../../img/icon2.jpg').convert()
icon3 = pygame.image.load('../../img/icon3.jpg').convert()

def getRandomGridValues():
  return random.randrange(gridnumbers),random.randrange(gridnumbers)


# 3 - Define game functions ####################################################
## 3a - Initialize the game board
def initBoard(): 
  for row in range(gridnumbers):
    grid.append([])
    for column in range(gridnumbers):
        grid[row].append(0) # all values set to 0
  # Set hard-coded start locations for player and icons:        
  grid[0][0] = 1  # player icon; value of 1 is player location
  x1,y1 = getRandomGridValues()
  while (x1,y1)==(0,0):
    x1,y1 = getRandomGridValues()
  x2,y2 = getRandomGridValues()
  while (x2,y2)==(x1,y1) or (x2,y2)==(0,0):
    x2,y2 = getRandomGridValues()
  x3,y3 = getRandomGridValues()
  while (x3,y3)==(x2,y2) or (x3,y3)==(x1,y1) or (x3,y3)==(0,0):
    x3,y3 = getRandomGridValues()
  x4,y4 = getRandomGridValues()
  while (x4,y4)==(x2,y2) or (x4,y4)==(x1,y1) or (x4,y4)==(x3,y3) or (x4,y4)==(0,0):
    x4,y4 = getRandomGridValues()
  grid[x1][y1] = 10 # icon 0 location set by a value of 10
  grid[x2][y2] = 11 # icon 1 location set by a value of 11
  grid[x3][y3] = 12 # icon 2 location set by a value of 12
  grid[x4][y4] = 13 # icon 3 location set by a value of 13

## 3b - Draw player/icon on the board
def drawIcon(rw,cl,iconName):
  screen.blit(iconName,((margin+width)*cl + margin,(margin+height)*rw + margin))
  
## 3c - Update the grid for the board
def updateBoard():
  for row in range(gridnumbers):
    for column in range(gridnumbers):
      color = WHITE             
      pygame.draw.rect(screen,color,[(margin + width) * column + margin,
                                     (margin + height) * row + margin,
                                      width, height])
      if grid[row][column] == 10:  #icon0 location
        drawIcon(row,column,icon0)  
      if grid[row][column] == 11:  #icon1 location
        drawIcon(row,column,icon1)  
      if grid[row][column] == 12:  #icon2 location
        drawIcon(row,column,icon2)  
      if grid[row][column] == 13:  #icon3 location
        drawIcon(row,column,icon3)    
      if grid[row][column] == 1:  #player location
        drawIcon(row,column,player)  

## 3d - Adjust score and print out a message if increased
def adjustScore(scoreP):
  if grid[playerCoord[0]][playerCoord[1]] >= 10:
    scoreP += 1
    print("You have learned "+str(scoreP)+" of the Core 4")
  return scoreP

## 3e - Handle player movement
def movePlayer(scoreParam):
  # Based on how-to at:
  # https://opensource.com/article/17/12/game-python-moving-player
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True; pygame.quit()
        sys.exit(); numlitter == 0
      # only handle key releases for simplicity (KEYUP not KEYDOWN)
      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == ord('a'):
          if playerCoord[1] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1          
        elif event.key == pygame.K_RIGHT or event.key == ord('d'):
          if playerCoord[1] < gridnumbers - 1:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[1] += 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1
        elif event.key == pygame.K_UP or event.key == ord('w'):
          if playerCoord[0] > 0:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] -= 1
            scoreParam = adjustScore(scoreParam)
            grid[playerCoord[0]][playerCoord[1]] = 1          
        elif event.key == pygame.K_DOWN or event.key == ord('s'):
          if playerCoord[0] < gridnumbers - 1:
            grid[playerCoord[0]][playerCoord[1]] = 0
            playerCoord[0] += 1
            scoreParam = adjustScore(scoreParam)    
            grid[playerCoord[0]][playerCoord[1]] = 1
        elif event.key == ord('q'):
          print('quit game'); pygame.quit()
          break          
  return scoreParam

# 4 - Define main game #########################################################
def gameFunct():
  ## 4a - Initialize game
  pygame.init()
  initBoard()
  clock = pygame.time.Clock()
  score = 0
  print("Collect all of the Core 4 to increase your knowledge!\n")
  ## 4b - keep looping until exit condition met
  while (score < 4):
    score = movePlayer(score)  # Handle player movement
    updateBoard() # Update the grid for the board
    clock.tick(60) # In milliseconds (https://www.pygame.org/docs/ref/time.html)
    pygame.display.flip() # Redraw the board
    if score == 4: # Check for exit condition congratulatory message
      print("Congratulations on learning all of the Core 4!")
      print("Now practice practice practice and create cool code!")
  pygame.quit() # Quit the game

# Run automatically upon load/F5 ###############################################
if __name__ == "__main__":
  gameFunct()
