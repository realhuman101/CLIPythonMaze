from src.characters.player import player
from src.map.grid import grid

from src.exceptions import *

import keyboard
import os
import time

SIZE = 15
WIDTH, HEIGHT = 27, 11

REFRESH = 0.01

board = grid(WIDTH, HEIGHT)
user = player(WIDTH, HEIGHT, 1, 0, board.maze)

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

    time.sleep(REFRESH)
