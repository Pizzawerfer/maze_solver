from window import Window, Point, Line
from maze import Cell
from constants import *

def main():
    print("Hello World!")
    win = Window(WIDTH,HEIGHT)
    # line1 = Line(Point(POINT1_X,POINT1_Y),Point(POINT2_X,POINT2_Y))
    # line2 = Line(Point(POINT2_X,POINT1_Y),Point(POINT1_X,POINT2_Y))
    # win.draw_line(line1,"black")
    # win.draw_line(line2,"blue")
    cell1 = Cell(CELL1_POS1,CELL1_POS2,win)
    cell2 = Cell(CELL2_POS1,CELL2_POS2,win,wall_b=False)
    cell3 = Cell(CELL3_POS1,CELL3_POS2,win,wall_t=False)
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell1.draw_move(cell2)
    cell2.draw_move(cell3, True)
    win.wait_for_close()
main()