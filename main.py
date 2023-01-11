from src.characters.player import player
from src.map.grid import grid

from src.exceptions import *

import keyboard
import os
import time

while True:
    try:
        width = int(input('Screen Width: '))
        break
    except ValueError:
        print('Please input an integer!')

while True:
    try:
        height = int(input('Screen Height: '))
        break
    except ValueError:
        print('Please input an integer!')

while True:
    try:
        refresh = int(input('Milliseconds wait per frame: '))/1000
        break
    except ValueError:
        print('Please input an integer!')

board = grid(width, height)
user = player(width, height, 1, 0, board.maze)

while True:
    if keyboard.is_pressed('w'):
        user.move('w')
    if keyboard.is_pressed('a'):
        user.move('a')
    if keyboard.is_pressed('s'):
        user.move('s')
    if keyboard.is_pressed('d'):
        user.move('d')
    
    os.system('clear') # 'cls'/'clear' based on your OS

    board.clear()
    board.change(user.x, user.y, user.char)
    board.print()

    time.sleep(refresh)
