from tkinter import Tk, BOTH, Canvas
from constants import *

class Window():
    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._canvas = Canvas(self._root, bg="grey", width=width,height=height)
        self._canvas.pack(fill=BOTH, expand=1)
        self._is_running = False
        self._root.protocol("WM_DELETE_WINDOW", self.close)
        
    def clear(self):
        self._canvas.delete("all")
        
    def redraw(self):
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        self._is_running = True
        while self._is_running == True:
            self.redraw()

    def close(self):
        self._is_running = False

    def draw_line(self, Line, fill_color):
        Line.draw(self._canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y
    
    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

class Line():
    def __init__(self, Point1, Point2):
        self._pos1 = (Point1.get_x(),Point1.get_y())
        self._pos2 = (Point2.get_x(),Point2.get_y())
        # print(self.__pos1)

    def get_coord(self):
        return self._pos1[0], self._pos1[1], self._pos2[0], self._pos2[1]
    
    def draw(self, Canvas, fill_color):
        x1,y1,x2,y2 = self.get_coord()
        Canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)