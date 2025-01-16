# from window import Window
from cell import Cell
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, canvas=None,seed=None):
        print("Generating ...")
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        if seed != None:
            self.seed = random.seed(seed)
        self._canvas = canvas
        self._create_cells()

    def solve(self):
        print("Solving...")
        return self._solve_r()

    def _create_cells(self):
        self._cells = []
        inner = []
        for num2 in range(self._num_cols):
            for num in range(self._num_rows):
                c = Cell(self._canvas)
                inner.append(c)
            self._cells.append(inner)
            inner = []

        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._draw_cell(col, row)
        
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        print("Maze generated and everything reset!")
        
    def _draw_cell(self, i, j):
        x = self._x1 + self._cell_size_x * i
        y = self._y1 + self._cell_size_y * j
        self._cells[i][j].draw(x, y, x+self._cell_size_x, y+self._cell_size_y)
        self._animate()

    def _animate(self):
        self._canvas.redraw()
        time.sleep(0.01)
        return
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            # time.sleep(0.25)
            lst = []
            if i-1 >= 0 and self._cells[i-1][j].visited == False:
                lst.append([i-1,j])
            if i+1 < self._num_cols and self._cells[i+1][j].visited == False:                
                lst.append([i+1,j])
            if j-1 >= 0 and self._cells[i][j-1].visited == False:                
                lst.append([i,j-1])
            if j+1 < self._num_rows and self._cells[i][j+1].visited == False:                
                lst.append([i,j+1])
                
            if len(lst) == 0:
                self._draw_cell(i,j)
                return  
            
            direction = random.choice(lst)
            if direction[0] < i:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if direction[0] > i:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            if direction[1] < j:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            if direction[1] > j:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False

            self._break_walls_r(direction[0],direction[1])
    
    def _reset_cells_visited(self):
        for col in range(len(self._cells)):
            for row in range(len(self._cells[col])):
                self._cells[col][row].visited = False

    def _solve_r(self, i=0, j=0):
        self._animate()
        self._cells[i][j].visited = True
        time.sleep(0.2)
        if i == self._num_cols-1 and j == self._num_rows-1:
            print("Solved!")
            return True
        
        if i+1 < self._num_cols and self._cells[i+1][j].visited == False and self._cells[i+1][j].has_left_wall == False:                
            self._cells[i][j].draw_move(self._cells[i+1][j], undo=True)
            if self._solve_r(i+1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j])
        if j+1 < self._num_rows and self._cells[i][j+1].visited == False and self._cells[i][j+1].has_top_wall == False:                
            self._cells[i][j].draw_move(self._cells[i][j+1], undo=True)
            if self._solve_r(i,j+1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1])
        if i-1 >= 0 and self._cells[i-1][j].visited == False and self._cells[i-1][j].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i-1][j], undo=True)
            if self._solve_r(i-1,j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j])
        if j-1 >= 0 and self._cells[i][j-1].visited == False and self._cells[i][j-1].has_bottom_wall == False:                
            self._cells[i][j].draw_move(self._cells[i][j-1], undo=True)
            if self._solve_r(i,j-1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1])
        
        
        return False