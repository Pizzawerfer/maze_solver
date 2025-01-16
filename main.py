from window import Window
from maze import Maze
from constants import *
import time
import random

def main():
    win = Window(WIDTH,HEIGHT)
    while True:
        num_rows = random.randrange(10,20)
        num_cols = random.randrange(10,20)
        margin = 50
        cell_size_x = (WIDTH - 2 * margin) / num_cols
        cell_size_y = (HEIGHT - 2 * margin) / num_rows
        c = Maze(margin, margin, num_rows,num_cols,cell_size_x,cell_size_y,win)
        c.solve()
        time.sleep(1)
        win.clear()
        print("Clearing the Canvas")
    win.wait_for_close()
main()