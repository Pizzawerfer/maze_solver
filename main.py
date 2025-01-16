from window import Window
from maze import Maze
from constants import *

def main():
    win = Window(WIDTH,HEIGHT)
    num_rows = 5
    num_cols = 5
    margin = 50
    cell_size_x = (WIDTH - 2 * margin) / num_cols
    cell_size_y = (HEIGHT - 2 * margin) / num_rows
    c = Maze(margin, margin, num_rows,num_cols,cell_size_x,cell_size_y,win,0)

    print(c.solve())
    win.wait_for_close()
main()