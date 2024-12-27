# Snake-Game
The snake game re-created in python
The program displays:
Dots for blank spaces "."
Hashtags for the snake "#"
Zeros for the apple "0"
The progrm keeps track of the snakes position by using an array of x and y coordinates,
The user can press wasd to change the direction of the snake.
The program calculates the next position of the snake and adds it to the position array shifting all the other coordinates down removing the first one unless the new position is equal to the apples location.
The program ends when the snake hits itself which is done by checking if there are two duplicates of x and y coordinates in the position array or when the snake exits the game boundaries.
