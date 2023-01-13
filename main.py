from src.characters.player import player
from src.map.grid import grid

from src.exceptions import *

import keyboard
import os
import time
import datetime

CLEAR = 'cls' # 'cls'/'clear' based on your OS

while True:
    try:
        width = int(input('Screen Width: '))
        if width <= 2:
            raise ValueError
        break
    except ValueError:
        print('Please input an integer or a number higher than 2!')

while True:
    try:
        height = int(input('Screen Height: '))
        if height <= 3:
            raise ValueError
        break
    except ValueError:
        print('Please input an integer or a number higher than 3!')

while True:
    try:
        refresh = int(input('Milliseconds wait per frame: '))/1000
        break
    except ValueError:
        print('Please input an integer!')

board = grid(width, height)
user = player(width, height, 1, 0, board.maze)

score = 0
completed = 0

beginTime = time.time()

while True:
    try:
        if keyboard.is_pressed('w'):
            user.move('w')
        if keyboard.is_pressed('a'):
            user.move('a')
        if keyboard.is_pressed('s'):
            user.move('s')
        if keyboard.is_pressed('d'):
            user.move('d')

    except ReachedEnd:
        os.system(CLEAR)

        completed += 1

        currTime = time.time()-beginTime

        addScore = round(3_600-currTime, 2) # 3,600 = 1 hour
        if addScore < 0: addScore = 0

        score += addScore

        print(f'Congratulations! You have reached the end of the maze!\nYou have completed a total of {completed} mazes!\nYou gained {addScore} points!\nYour total score is currently {score}!')

        if ('y' not in input('Would you like to play again? ').lower()):
            break
        
        board.newMaze()
        user = player(width, height, 1, 0, board.maze)
        beginTime = time.time()
    
    os.system(CLEAR)

    board.clear()
    board.change(user.x, user.y, user.char)
    board.print()
    print(f'\n\nScore: {score}\nTimer: {str(datetime.timedelta(seconds=time.time()-beginTime))}')

    time.sleep(refresh)
