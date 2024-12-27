import random
import time
import keyboard
import sys

difficulty = ""
snake_pos = [[0, -2], [0, -1], [0, 0]]
check = [0, 0]
indexcheck = 0
direction = "right"
new_pos = [0, 0]
apple = [0,0]


def display():
    for a in range (-5, 5):
        print (end = "\n")
        for b in range (-5, 5):
            check = [a, b]
            if check in snake_pos:
                print ("#", end = "")
            elif check == apple:
                print ("0", end = "")
            else:
                print(".", end = "")


def controller():
    if keyboard.is_pressed("w"):
        return "up"
    elif keyboard.is_pressed("d"):
        return "right"
    elif keyboard.is_pressed("s"):
        return "down"
    elif keyboard.is_pressed("a"):
        return "left"
    else:
        return direction


def over_check():
    for i in range(len(snake_pos)):


        if snake_pos.count(snake_pos[i]) == 2:

            return "x"
    new_pos = snake_pos[len(snake_pos) - 1].copy()
    if new_pos[0] < -5 or new_pos[0] > 4 or new_pos[1] < -5 or new_pos[1] > 4:
        return  "x"

difficulty = str(input("Choose diffuculty"))
if difficulty == "easy":
    difficulty = 1
elif difficulty =="normal":
    difficulty = 0.75
else:
    difficulty = 0.5

def move(x, y):
    global apple
    new_pos = snake_pos[len(snake_pos) - 1].copy()
    new_pos[x] += y
    if new_pos != apple:
        snake_pos.pop(0)
    if new_pos == apple:
        apple = [random.randint(-5, 4), random.randint(-5, 4)]
        while apple in snake_pos or new_pos == apple:
            apple = [random.randint(-5, 4), random.randint(-5, 4)]
    snake_pos.append(new_pos)
    display()


start_time = time.time()
apple = [random.randint(-5, 4), random.randint(-5, 4)]



while True:
    start_time = time.time()
    elapsed_time = 0


    while elapsed_time < difficulty:
        elapsed_time = time.time() - start_time

        direction = (controller())


    if direction == "up":
        move(0, -1)
    if direction ==  "down":
        move(0, 1)
    if direction == "right":
        move(1, 1)
    if direction == "left":
       move (1, -1)

    if over_check() == "x":
        sys.exit()
    print (end = "\n")
