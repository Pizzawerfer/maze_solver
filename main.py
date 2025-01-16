from window import Window
from maze import Maze
from constants import *

def main():
    print("Hello World!")
    win = Window(WIDTH,HEIGHT)
    num_rows = 10
    num_cols = 10
    margin = 50
    cell_size_x = (WIDTH - 2 * margin) / num_cols
    cell_size_y = (HEIGHT - 2 * margin) / num_rows
    c = Maze(margin, margin, num_rows,num_cols,cell_size_x,cell_size_y,win)
    
    win.wait_for_close()
main()