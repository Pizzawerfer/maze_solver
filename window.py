from tkinter import Tk, BOTH, Canvas
from constants import *

class Window():
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width=width,height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running == True:
            self.redraw()

    def close(self):
        self.__is_running = False

    def draw_line(self, Line, fill_color):
        Line.draw(self.__canvas, fill_color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, Point1, Point2):
        self.__pos1 = (Point1.x,Point1.y)
        self.__pos2 = (Point2.x,Point2.y)
        # print(self.__pos1)

    def get_coord(self):
        return self.__pos1[0], self.__pos1[1], self.__pos2[0], self.__pos2[1]
    
    def draw(self, Canvas, fill_color):
        x1,y1,x2,y2 = self.get_coord()
        Canvas.create_line(x1, y1, x2, y2, fill=fill_color, width=2)