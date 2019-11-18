# M6: Core 4: Functions
[18 NOV 2019]

## What is a function?
**The computer can bundle commands and refer back to these bundles when you need them**

A function is a set of commands that produces a specific action. Some languages have built-in functions, such as `print( )` in Python, and move in Scratch. Most languages will also let programmers write their own functions. Programmers use functions to create a process that can easily be used and reused in their code, rather than writing out the process every time.

<p align="center">
     <img src="../../img/functions.PNG"
          alt="functions diagram"
          height="350"/>
</p>


## Recognize what functions and using functions look like in Python
1. Using Windows file explorer, find the folder with the Python games and right click and open both games in IDLE: basicGame2019.py and functionGame2019.py -- if you've changed the basicGame2019.py code, rename your changed code (as per Add Content #2 at https://github.com/jinnyyan/gwc19-game/blob/master/lessons/python/M5gitGood.md) and pull a fresh copy of the repository.
1. Set up your windows so you can see both at one time (with one IDLE window selected, you could press the Windows button and the left arrow at once -- WIN + left, and then the Windows button and the right arrow for the other window -- WIN + right).
1. Do these games play exactly the same? F5 both of the games to check by playing through them.
1. How many lines start with `def` in the basic game? How many lines start with `def` in the function game?
1. On what column do all of the `def` function keywords start? How do you know when you are at the end of that function?
1. Find all occurences of the function name `initBoard` (use CTRL+f to do this, or go to Edit --> Find). How many times does this function name occur? The first time it occurs is when it is used to define a function following the keyword `def`. The second time it occurs is when we call this function to do the bundled commands it defines (no `def` in the function call!). When a function gets called, it is followed by parentheses `()` and any parameters that we should use when doing the function's bundled commands (like putting a value for all occurences of 'x' in a mathematical function).
1. Find all occurences of the `adjustScore` function. How many times is it defined with `def`? How many times is it called?

## Identify and change functions in the game
1. After the movePlayer function and prior to the gameFunct (and its comment `# 4 - Define main game ###`), create a new function using the below code and your own message:
```python
def welcomeMsg():
  print("\nHello and welcome to <my name>'s game!")
  print("I hope you enjoy playing :)")
```
..* Note: the "\n" character tells the computer to give you a new line prior to the word "Hello".
1. Save and run the game (CTRL+s and F5). Why didn't your function run?
1. Within `## 4a - Initialize game` and prior to `## 4b - keep looping until exit condition met`, call your new function:
```python
  welcomeMsg()
```
..* Make sure it's at the same indentation as the other commands in 4a!
1. Save and run the game. Did it work?
1. One of the commands within the 4a set would work better in your new function -- the other print command! Move it to your welcomeMsg function, save, and run again.

## Add a help function (intermediate)
1. After the welcomeMsg function and before the gameFunct function, add a new function named helpMsg():
```python
def helpMsg(scoreParam):
  welcomeMsg()
  print("You have collected "+str(scoreParam)+" of the Core 4")
```
1. In the movePlayer function, add a selection statement to call your help function when the player presses the 'h' key. Find where the first four lines shown below occur and add the last two lines above `elif` in that function:
```python
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
        done = True; pygame.quit()
        sys.exit(); numlitter == 0
      if event.key == ord('h'):
        helpMsg(scoreParam) 
```

## Reflect
The goal of functions is to make it easier to do the same bundle of commands repeatedly -- think about cases where this is useful and helps makes things more efficient. 
* Are there cases where it may be better to not use functions? 
* basicGame2019.py has 118 lines and functionGame2019.py has 126 lines. Is there a specific number of lines at which using functions makes more sense and helps keep your code organized?
* Is it easier to troubleshoot bugs/errors in your code with or without functions? Why/why not?