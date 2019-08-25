// Based on code at:
// https://codepen.io/TheCodeDepository/pen/jKBaoN?page=8
// This code is created for Girls Who Code Augusta University 

// Current TODO:
// - Add logic that game can't be completed without gathering all modules
// - Move alert container to the side instead of front with button dismissing it
// - Add logic to ensure core modules don't choose the same random spot


// Question to GWC: What does this function do? What is the point of using max, random, and floor? Extensibility?
function rand(max) {
  return Math.floor(Math.random() * max);
}

// Question to GWC: Ways to improve this function, using rand(max) above?
function shuffle(a) {
  for (let i = a.length - 1; i > 0; i--) { // Question to GWC: Walk us through this for loop, what does i-- mean?
    const j = Math.floor(Math.random() * (i + 1)); // Answer: rand(i + 1)
    [a[i], a[j]] = [a[j], a[i]]; // Question to GWC: What does this do?
  }
  return a;
}

// Question to GWC: When does this function matter and come into play?
function displayVictoryMess(moves) {
  document.getElementById("moves").innerHTML = "You Moved " + moves + " Steps.";
  toggleVisablity("Message-Container");  
}

// Task to GWC: Create message container that says "You Found Core Module __!" (complete)
function displayCoreMess(coreNum) {
  document.getElementById("moves").innerHTML = "You Found Core Module " + coreNum + "!";
  toggleVisablity("Message-Container");
}

// Used to check if an array of coords includes a specific coord
function coordIncludes(coordList, coord){
  var coordListX = coordList.map((n) => { return n.x })
  var coordListY = coordList.map((n) => { return n.y })
  if (coordListX.includes(coord.x) && (coordListY.includes(coord.y))){
    if (coordListX.indexOf(coord.x)===coordListY.indexOf(coord.y)){
      return coordListX.indexOf(coord.x) + 1 // Add 1 to offset that array starts from 0
    }
  } 
  return 0; 
}

// Question to GWC: What does this function do? What is the visibility property?
function toggleVisablity(id) { // Answer: Used for the victory message
  if (document.getElementById(id).style.visibility == "visible") {
    document.getElementById(id).style.visibility = "hidden";
  } else {
    document.getElementById(id).style.visibility = "visible";
  }
}

// Object-Oriented concept for higher levels.
function Maze(Width, Height) {
  var mazeMap;
  var width = Width;
  var height = Height;
  var startCoord, endCoord, coreCoord;
  var dirs = ["n", "s", "e", "w"]; // North, South, East, West
  var modDir = {
    n: {
      y: -1,
      x: 0,
      o: "s" // o = opposite
    },
    s: {
      y: 1,
      x: 0,
      o: "n"
    },
    e: {
      y: 0,
      x: 1,
      o: "w"
    },
    w: {
      y: 0,
      x: -1,
      o: "e"
    }
  };

  // Accessing object oriented attributes of the map
  this.map = function() {
    return mazeMap;
  };
  this.startCoord = function() {
    return startCoord;
  };
  this.endCoord = function() {
    return endCoord;
  };
  this.coreCoord = function() {
    return coreCoord;
  }

  // Generate a map that is an array of arrays (height x width)
  function genMap() {
    mazeMap = new Array(height);
    for (y = 0; y < height; y++) {
      mazeMap[y] = new Array(width);
      for (x = 0; x < width; ++x) {
        mazeMap[y][x] = { // Each block in map has the following properties
          n: false,
          s: false,
          e: false,
          w: false,
          visited: false,
          priorPos: null
        };
      }
    }
  }

  // In order to check moves and current positions
  function defineMaze() {
    var isComp = false;
    var move = false;
    var cellsVisited = 1;
    var numLoops = 0;
    var maxLoops = 0;
    var pos = {
      x: 0,
      y: 0
    };
    var numCells = width * height;
    while (!isComp) { // While not completed
      move = false;
      mazeMap[pos.x][pos.y].visited = true; // Mark location as visited

      if (numLoops >= maxLoops) {
        shuffle(dirs);
        maxLoops = Math.round(rand(height / 8));
        numLoops = 0;
      }
      numLoops++;
      for (index = 0; index < dirs.length; index++) {
        var direction = dirs[index];
        var nx = pos.x + modDir[direction].x;
        var ny = pos.y + modDir[direction].y;

        if (nx >= 0 && nx < width && ny >= 0 && ny < height) {
          //Check if the tile is already visited
          if (!mazeMap[nx][ny].visited) {
            //Carve through walls from this tile to next
            mazeMap[pos.x][pos.y][direction] = true;
            mazeMap[nx][ny][modDir[direction].o] = true;

            //Set Currentcell as next cells Prior visited
            mazeMap[nx][ny].priorPos = pos;
            //Update Cell position to newly visited location
            pos = {
              x: nx,
              y: ny
            };
            cellsVisited++;
            //Recursively call this method on the next tile
            move = true;
            break;
          }
        }
      }

      if (!move) {
        //  If it failed to find a direction,
        //  move the current position back to the prior cell and Recall the method.
        pos = mazeMap[pos.x][pos.y].priorPos;
      }
      if (numCells == cellsVisited) {
        isComp = true; // If it touched every cell, then marks as completed
      }
    }
  }

  // Randomly choose where the end is four 4 possible cases
  function defineStartEnd() {
    switch (rand(4)) {
      case 0: // Start top left, end bottom right
        console.log("Case 0");
        startCoord = {
          x: 0,
          y: 0
        };
        endCoord = {
          x: height - 1,
          y: width - 1
        };
        break;
      case 1: // Start bottom left, end top right
        console.log("Case 1");
        startCoord = {
          x: 0,
          y: width - 1
        };
        endCoord = {
          x: height - 1,
          y: 0
        };
        break;
      case 2: // Start top right, end bottom left
        console.log("Case 2");
        startCoord = {
          x: height - 1,
          y: 0
        };
        endCoord = {
          x: 0,
          y: width - 1
        };
        break;
      case 3: // Start bottom right, end top left
      console.log("Case 3");
        startCoord = {
          x: height - 1,
          y: width - 1
        };
        endCoord = {
          x: 0,
          y: 0
        };
        break;
    }
  }

  function randomCoord() {
    var randomX = rand(difficulty);  
    var randomY = rand(difficulty);
    if (randomX==endCoord.x && randomY==endCoord.y){
      console.log("Regenerate new random coord for mid sprite to avoid final");
      randomX = rand(difficulty);
      randomY = rand(difficulty);
    }
    coord = { x: randomX, y: randomY };
    return coord; 
  }

  function defineOtherSprites() {
    var sprite1Coord = randomCoord();
    var sprite2Coord = randomCoord();
    var sprite3Coord = randomCoord();
    coreCoord = [sprite1Coord, sprite2Coord, sprite3Coord];
  }

  genMap();
  defineStartEnd();
  defineOtherSprites();
  defineMaze();
}

// This class does all the maze drawing!
function DrawMaze(Maze, ctx, cellsize, midSprites, sprite4) {
  var map = Maze.map();
  var cellSize = cellsize;
  ctx.lineWidth = cellSize / 40;

  this.redrawMaze = function(size) {
    cellSize = size;
    ctx.lineWidth = cellSize / 50;
    drawMap();
    drawMidSprites(sprite1, sprite2, sprite3);
    drawEndSprite(sprite4);
  };

  // Determine which paths are "false" and draw line to block direction
  function drawCell(xCord, yCord, cell) {
    var x = xCord * cellSize;
    var y = yCord * cellSize;

    if (cell.n == false) {
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x + cellSize, y);
      ctx.stroke();
    }
    if (cell.s === false) {
      ctx.beginPath();
      ctx.moveTo(x, y + cellSize);
      ctx.lineTo(x + cellSize, y + cellSize);
      ctx.stroke();
    }
    if (cell.e === false) {
      ctx.beginPath();
      ctx.moveTo(x + cellSize, y);
      ctx.lineTo(x + cellSize, y + cellSize);
      ctx.stroke();
    }
    if (cell.w === false) {
      ctx.beginPath();
      ctx.moveTo(x, y);
      ctx.lineTo(x, y + cellSize);
      ctx.stroke();
    }
  }
  
  // This calls on drawCell for every cell in map
  function drawMap() {
    for (x = 0; x < map.length; x++) {
      for (y = 0; y < map[x].length; y++) {
        drawCell(x, y, map[x][y]);
      }
    }
  }

  // Handle the final sprite (core 4!)
  function drawEndSprite(sprite) {
    var offsetLeft = cellSize / 50;
    var offsetRight = cellSize / 25;
    var coord = Maze.endCoord();
    ctx.drawImage(
      sprite,
      2,
      2,
      sprite.width,
      sprite.height,
      coord.x * cellSize + offsetLeft,
      coord.y * cellSize + offsetLeft,
      cellSize - offsetRight,
      cellSize - offsetRight
    );
  }

  // Handle each of the middle sprites
  function drawMidSprites(sprites) {
    var offsetLeft = cellSize / 50;
    var offsetRight = cellSize / 25;
    var coreCoord = Maze.coreCoord();
    for (i = 0; i < coreCoord.length; i++) { 
      var coord = coreCoord[i];
      var sprite = sprites[i];
      ctx.drawImage(
        sprites[i],
        2,
        2,
        sprite.width,
        sprite.height,
        coord.x * cellSize + offsetLeft,
        coord.y * cellSize + offsetLeft,
        cellSize - offsetRight,
        cellSize - offsetRight
      );
    }
  }

  function clear() { // Defined and used once.
    var canvasSize = cellSize * map.length;
    ctx.clearRect(0, 0, canvasSize, canvasSize);
  }

  clear();
  drawMap();
  drawMidSprites(midSprites);
  drawEndSprite(sprite4);
}

// Advanced Object Oriented concept for higher levels.
function Player(maze, c, _cellsize, onComplete, sprite) {
  var ctx = c.getContext("2d");
  var moves = 0;
  var player = this;
  var map = maze.map();
  var cellCoords = {
    x: maze.startCoord().x,
    y: maze.startCoord().y
  };
  var cellSize = _cellsize;

  this.redrawPlayer = function(_cellsize) {
    cellSize = _cellsize;
    drawSpriteImg(cellCoords);
  };

  function drawSpriteImg(coord) {
    var offsetLeft = cellSize / 50;
    var offsetRight = cellSize / 25;
    ctx.drawImage(
      sprite,
      0,
      0,
      sprite.width,
      sprite.height,
      coord.x * cellSize + offsetLeft,
      coord.y * cellSize + offsetLeft,
      cellSize - offsetRight,
      cellSize - offsetRight
    );
    // If coordinates of player reaches end, show display box and trigger complete, stop key trigger
    if (coord.x === maze.endCoord().x && coord.y === maze.endCoord().y) {
      onComplete(moves);
      player.unbindKeyDown();
    }
    // Checking for whether the coordinates are within the random sprint cores
    var coreNum = coordIncludes(maze.coreCoord(),coord)
    if (coreNum != 0) { // Means that no coreNum was reached
      console.log('Reached a core module!');
      // TODO: Remove coordinates so that if you go back, the alert doesn't come up again
      displayCoreMess(coreNum);
    }
    // TASK TO GWC: Extend this to identify when other core modules have been reached. (complete)
  }

  function removeSprite(coord) {
    var offsetLeft = cellSize / 50;
    var offsetRight = cellSize / 25;
    ctx.clearRect(
      coord.x * cellSize + offsetLeft,
      coord.y * cellSize + offsetLeft,
      cellSize - offsetRight,
      cellSize - offsetRight
    );
  }

  // This function takes the key pressed, removes player sprite from location and puts it at new location
  function check(e) {
    var cell = map[cellCoords.x][cellCoords.y];
    moves++;
    switch (e.keyCode) {
      case 65:
      case 37: // west
        if (cell.w == true) {
          removeSprite(cellCoords); // Removes player sprite and core sprite
          cellCoords = {
            x: cellCoords.x - 1,
            y: cellCoords.y
          };
          drawSpriteImg(cellCoords);
        }
        break;
      case 87:
      case 38: // north
        if (cell.n == true) {
          removeSprite(cellCoords);
          cellCoords = {
            x: cellCoords.x,
            y: cellCoords.y - 1
          };
          drawSpriteImg(cellCoords);
        }
        break;
      case 68:
      case 39: // east
        if (cell.e == true) {
          removeSprite(cellCoords);
          cellCoords = {
            x: cellCoords.x + 1,
            y: cellCoords.y
          };
          drawSpriteImg(cellCoords);
        }
        break;
      case 83:
      case 40: // south
        if (cell.s == true) {
          removeSprite(cellCoords);
          cellCoords = {
            x: cellCoords.x,
            y: cellCoords.y + 1
          };
          drawSpriteImg(cellCoords);
        }
        break;
    }
  }

  // Binds the key input to actions
  this.bindKeyDown = function() {
    window.addEventListener("keydown", check, false);
    // Checks for swipes (mobile and computer)
    $("#view").swipe({
      swipe: function(
        direction
      ) {
        switch (direction) {
          case "up":
            check({
              keyCode: 38
            });
            break;
          case "down":
            check({
              keyCode: 40
            });
            break;
          case "left":
            check({
              keyCode: 37
            });
            break;
          case "right":
            check({
              keyCode: 39
            });
            break;
        }
      },
      threshold: 0
    });
  };

  // This function clears the bind from key to action
  this.unbindKeyDown = function() {
    window.removeEventListener("keydown", check, false);
    $("#view").swipe("destroy");
  };

  drawSpriteImg(maze.startCoord());

  this.bindKeyDown();
}

var mazeCanvas = document.getElementById("mazeCanvas");
var ctx = mazeCanvas.getContext("2d");
var playerSprite;
var core1Sprite;
var core2Sprite;
var core3Sprite;
var core4Sprite;
var maze, draw, player;
var cellSize;
var difficulty;

// This function gets activate when the page loads
window.onload = function() {
  console.log("window has been onload");
  let viewWidth = $("#view").width();
  let viewHeight = $("#view").height();
  // Edit view height and width to create perfectly square canvas that fits the whole page
  if (viewHeight < viewWidth) {
    ctx.canvas.width = viewHeight - viewHeight / 100;
    ctx.canvas.height = viewHeight - viewHeight / 100;
  } else {
    ctx.canvas.width = viewWidth - viewWidth / 100;
    ctx.canvas.height = viewWidth - viewWidth / 100;
  }

  // Load player sprite
  playerSprite = new Image();
  playerSprite.src = "../img/player.png";
  playerSprite.onload = function() {
    completeOne = true;
  };

  // Load core module sprites
  var imgArray = [
    "/img/icon0.png",
    "/img/icon1.png",
    "/img/icon2.png",
    "/img/icon3.png"]
  core1Sprite = new Image();
  core1Sprite.src = imgArray[0];
  core2Sprite = new Image();
  core2Sprite.src = imgArray[1];
  core3Sprite = new Image();
  core3Sprite.src = imgArray[2];
  core4Sprite = new Image();
  core4Sprite.src = imgArray[3];

  // Send it!
  console.log("Ready to go!");
  setTimeout(function(){
    makeMaze();
  }, 500);

};

// When window is resized, the width and height of the cell adapt accordingly
window.onresize = function() {
  let viewWidth = $("#view").width();
  let viewHeight = $("#view").height();
  if (viewHeight < viewWidth) {
    ctx.canvas.width = viewHeight - viewHeight / 100;
    ctx.canvas.height = viewHeight - viewHeight / 100;
  } else {
    ctx.canvas.width = viewWidth - viewWidth / 100;
    ctx.canvas.height = viewWidth - viewWidth / 100;
  }
  cellSize = mazeCanvas.width / difficulty;
  if (player != null) {
    draw.redrawMaze(cellSize);
    player.redrawPlayer(cellSize);
  }
};

// Main function that gets reloaded on button click, gets called on window load
function makeMaze() {
  if (player != undefined) {
    player.unbindKeyDown();
    player = null;
  }
  // Choose difficulty from dropdown menu
  var e = document.getElementById("diffSelect");
  difficulty = e.options[e.selectedIndex].value;
  console.log("This is the difficulty score: " + difficulty);
  
  // Generate cell size from difficulty score (changed from index.html)
  cellSize = mazeCanvas.width / difficulty;
  maze = new Maze(difficulty, difficulty);
  var coreMidSprites = [core1Sprite, core2Sprite, core3Sprite];
  draw = new DrawMaze(maze, ctx, cellSize, coreMidSprites, core4Sprite);
  player = new Player(maze, mazeCanvas, cellSize, displayVictoryMess, playerSprite);
  
  // Fix up opacity of maze container
  if (document.getElementById("mazeContainer").style.opacity < "100") {
    document.getElementById("mazeContainer").style.opacity = "100";
  }
}