from window import *
from cell import Cell
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, canvas=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._canvas = canvas
        self._create_cells()

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
        
    def _draw_cell(self, i, j):
        x = self._x1 + self._cell_size_x * i
        y = self._y1 + self._cell_size_y * j
        self._cells[i][j].draw(x, y, x+self._cell_size_x, y+self._cell_size_y)
        self._animate()

    def _animate(self):
        self._canvas.redraw()
        time.sleep(0.025)