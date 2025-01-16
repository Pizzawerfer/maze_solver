from window import *

class Cell():
    def __init__(self, Canvas=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._canvas = Canvas

    def draw(self, x1, y1, x2, y2):
        point_tl = Point(x1, y1)
        point_tr = Point(x2, y1)
        point_bl = Point(x1, y2)
        point_br = Point(x2, y2)

        if self.has_left_wall:
            line_left = Line(point_bl, point_tl)
            self._canvas.draw_line(line_left, "black")

        if self.has_right_wall:
            line_right = Line(point_br, point_tr)
            self._canvas.draw_line(line_right, "black")

        if self.has_top_wall:
            line_top = Line(point_tl, point_tr)
            self._canvas.draw_line(line_top, "black")

        if self.has_bottom_wall:
            line_bottom = Line(point_bl, point_br)
            self._canvas.draw_line(line_bottom, "black")

    def get_midpoint(self):
        midpoint_self_x = (self._x1 + self._x2) // 2
        midpoint_self_y = (self._y1 + self._y2) // 2
        return Point(midpoint_self_x, midpoint_self_y)

    def draw_move(self, to_cell, undo=False):
        mid_self = self.get_midpoint()
        mid_cell = to_cell.get_midpoint()
        line = Line(mid_self,mid_cell)
        if undo:
            color = "grey"
        else:
            color = "red"
        self._canvas.draw_line(line,color)