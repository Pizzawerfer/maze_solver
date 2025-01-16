from window import *

class Cell():
    def __init__(self, Pos1, Pos2, Canvas, wall_l=True, wall_r=True, wall_t=True, wall_b=True):
        self.has_left_wall = wall_l
        self.has_right_wall = wall_r
        self.has_top_wall = wall_t
        self.has_bottom_wall = wall_b
        self.__x1 = Pos1[0]
        self.__y1 = Pos1[1]
        self.__x2 = Pos2[0]
        self.__y2 = Pos2[1]
        self.__canvas = Canvas

    def draw(self):
        point_tl = Point(self.__x1,self.__y1)
        point_tr = Point(self.__x2,self.__y1)
        point_bl = Point(self.__x1,self.__y2)
        point_br = Point(self.__x2,self.__y2)

        if self.has_left_wall:
            line_left = Line(point_bl, point_tl)
            self.__canvas.draw_line(line_left, "black")

        if self.has_right_wall:
            line_right = Line(point_br, point_tr)
            self.__canvas.draw_line(line_right, "black")

        if self.has_top_wall:
            line_top = Line(point_tl, point_tr)
            self.__canvas.draw_line(line_top, "black")

        if self.has_bottom_wall:
            line_bottom = Line(point_bl, point_br)
            self.__canvas.draw_line(line_bottom, "black")