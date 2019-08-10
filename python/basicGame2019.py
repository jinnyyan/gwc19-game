# Based on code at:
# http://programarcadegames.com/python_examples/f.php?file=array_backed_grid.py

# 1 - Import library
import pygame
from pygame.locals import *

# 2 - Initialize the game
boardsize = (512, 512)
screen = pygame.display.set_mode(boardsize)
width, height, margin = 100, 100, 2

BLACK = (0, 0, 0)
WHITE = (255,255,255)
trigger = 1

## 2D array (list of lists)
grid = []
for row in range(5):
    grid.append([])
    for column in range(5):
        grid[row].append(0)

pygame.init()

player = pygame.image.load('../img/player.jpg').convert()
playerCoord = [0,0]
grid[0][0] = 1 #player icont; value of 1 is player location

icon0 = pygame.image.load('../img/icon0.jpg').convert()
##icon0Coord = [0,2]
grid[0][2] = 10
icon1 = pygame.image.load('../img/icon1.jpg').convert()
##icon1Coord = [3,1]
grid[3][1] = 11
icon2 = pygame.image.load('../img/icon2.jpg').convert()
##icon2Coord = [2,2]
grid[2][2] = 12
icon3 = pygame.image.load('../img/icon3.jpg').convert()
##icon3Coord = [4,3]
grid[4][3] = 13

clock = pygame.time.Clock()
score = 0
print("Collect all of the Core 4 to increase your knowledge!\n")

# 5 - keep looping through until condition met
while (score < 4):

# Move player based on how-to at:
# https://opensource.com/article/17/12/game-python-moving-player
  for event in pygame.event.get():
    if event.type == pygame.QUIT or trigger == 0:
      done = True; pygame.quit()
      sys.exit(); numlitter == 0
    # only handle key releases for simplicity (KEYUP not KEYDOWN)
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key == ord('a'):
##        print('left release')
##        print(playerCoord[0],playerCoord[1])
        if playerCoord[1] > 0:
          grid[playerCoord[0]][playerCoord[1]] = 0
          playerCoord[1] -= 1
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4") 
          grid[playerCoord[0]][playerCoord[1]] = 1          
      elif event.key == pygame.K_RIGHT or event.key == ord('d'):
##        print('right release')
##        print(playerCoord[0],playerCoord[1])
        if playerCoord[1] < 4:
          grid[playerCoord[0]][playerCoord[1]] = 0
          playerCoord[1] += 1
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4")           
          grid[playerCoord[0]][playerCoord[1]] = 1
      elif event.key == pygame.K_UP or event.key == ord('w'):
##        print('up release')
##        print(playerCoord[0],playerCoord[1])
        if playerCoord[0] > 0:
          grid[playerCoord[0]][playerCoord[1]] = 0
          playerCoord[0] -= 1
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4")           
          grid[playerCoord[0]][playerCoord[1]] = 1          
      elif event.key == pygame.K_DOWN or event.key == ord('s'):
##        print('down release')
##        print(playerCoord[0],playerCoord[1])
        if playerCoord[0] < 4:
          grid[playerCoord[0]][playerCoord[1]] = 0
          playerCoord[0] += 1
          if grid[playerCoord[0]][playerCoord[1]] >= 10:
            score += 1
            print("You have learned "+str(score)+" of the Core 4")           
          grid[playerCoord[0]][playerCoord[1]] = 1
      elif event.key == ord('q'):
        print('quit game'); pygame.quit()
        trigger = 0; break
        
  #reset screen
  if trigger > 0:
    screen.fill(BLACK)        
      
  # Draw the grid
  for row in range(5):
      for column in range(5):
          color = WHITE             
          pygame.draw.rect(screen,color,
                           [(margin + width) * column + margin,
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

  #update clock for next frame in milliseconds
  #reference https://www.pygame.org/docs/ref/time.html
  clock.tick(60) 

  #redraw board
  pygame.display.flip()

  if score == 4:   
    print("Congratulations on learning all of the Core 4!")
    print("Now practice practice practice and create cool code!")
pygame.quit()
