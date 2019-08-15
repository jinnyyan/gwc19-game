# Based on code at:
# http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# 1 - Import pygame library
import pygame
from pygame.locals import *

# 2 - Set game global variables
boardsize = (512, 512)
screen = pygame.display.set_mode(boardsize)
width, height, margin = 100, 100, 2
BLACK = (0, 0, 0)
WHITE = (255,255,255)

# Set up 2D array (list of lists) for board
grid = []
for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0) # all values set to 0

# Set hard-coded start locations for player and icons:
player = pygame.image.load('../img/player.jpg').convert()
playerCoord = [0,0]
grid[0][0] = 1 # player icon; value of 1 is player location
icon0 = pygame.image.load('../img/icon0.jpg').convert()
grid[0][2] = 10 # icon 0 location set by a value of 10
icon1 = pygame.image.load('../img/icon1.jpg').convert()
grid[3][1] = 11 # icon 1 location set by a value of 11
icon2 = pygame.image.load('../img/icon2.jpg').convert()
grid[2][2] = 12 # icon 2 location set by a value of 12
icon3 = pygame.image.load('../img/icon3.jpg').convert()
grid[4][3] = 13 # icon 3 location set by a value of 13

pygame.init()
clock = pygame.time.Clock()
score = 0
print("Collect all of the Core 4 to increase your knowledge!\n")

# 5 - keep looping until exit condition met
while (score < 4):

  # Move player based on how-to at:
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
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4") 
          grid[playerCoord[0]][playerCoord[1]] = 1          
      elif event.key == pygame.K_RIGHT or event.key == ord('d'):
        if playerCoord[1] < 4:
          grid[playerCoord[0]][playerCoord[1]] = 0
          playerCoord[1] += 1
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4")           
          grid[playerCoord[0]][playerCoord[1]] = 1
      elif event.key == pygame.K_UP or event.key == ord('w'):
        if playerCoord[0] > 0:
          grid[playerCoord[0]][playerCoord[1]] = 0
          playerCoord[0] -= 1
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4")           
          grid[playerCoord[0]][playerCoord[1]] = 1          
      elif event.key == pygame.K_DOWN or event.key == ord('s'):
        if playerCoord[0] < 4:
          grid[playerCoord[0]][playerCoord[1]] = 0
          playerCoord[0] += 1
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4")           
          grid[playerCoord[0]][playerCoord[1]] = 1
      elif event.key == ord('q'):
        print('quit game'); pygame.quit()
        break
             
  # Update the grid for the board
  for row in range(5):
      for column in range(5):
          color = WHITE             
          pygame.draw.rect(screen,color,[(margin + width) * column + margin,
                                         (margin + height) * row + margin,
                                          width, height])
          if grid[row][column] == 10:  #icon0 location
              screen.blit(icon0,((margin+width)*column + margin,
                                 (margin+height)*row+margin))
          if grid[row][column] == 11:  #icon1 location
              screen.blit(icon1,((margin+width)*column + margin,
                                 (margin+height)*row+margin))
          if grid[row][column] == 12:  #icon2 location
              screen.blit(icon2,((margin+width)*column + margin,
                                 (margin+height)*row+margin))
          if grid[row][column] == 13:  #icon3 location
              screen.blit(icon3,((margin+width)*column + margin,
                                 (margin+height)*row+margin))                        
          if grid[row][column] == 1:  #player location
              screen.blit(player,((margin+width)*column + margin,
                                 (margin+height)*row+margin))

  clock.tick(60) # In milliseconds (https://www.pygame.org/docs/ref/time.html)
  pygame.display.flip() # Redraw the board
  
  if score == 4: # Check for exit condition congratulatory message
    print("Congratulations on learning all of the Core 4!")
    print("Now practice practice practice and create cool code!")
    
pygame.quit() # Quit the game