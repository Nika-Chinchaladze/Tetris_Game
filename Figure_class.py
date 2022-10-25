from turtle import Turtle
from random import randint
SQUARE_POSITIONS = [(-180, 320), (-180, 360), (-140, 360), (-140, 320)]
H_RECTANGLE_POSITIONS = [(-180, 320), (-140, 320), (-100, 320), (-60, 320)]
V_RECTANGLE_POSITIONS = [(-180, 320), (-180, 360), (-180, 400), (-180, 440)]
RIGHT_CORNER_POSITIONS = [(-180, 320), (-140, 320), (-140, 360), (-100, 360)]
LEFT_CORNER_POSITIONS = [(-180, 360), (-140, 360), (-140, 320), (-100, 320)]
STEP_LEFT_POSITIONS = [(-180, 360), (-140, 400), (-140, 360), (-140, 320)]
STEP_RIGHT_POSITIONS = [(-180, 320), (-180, 360), (-180, 400), (-140, 360)]
FRONT_ARROW_POSITIONS = [(-180, 320), (-140, 320), (-140, 360), (-100, 320)]
BACK_ARROW_POSITIONS = [(-180, 360), (-140, 360), (-140, 320), (-100, 360)]
L_POSITIONS = [(-180, 320), (-180, 360), (-180, 400), (-140, 320)]
R_POSITIONS = [(-180, 320), (-140, 360), (-140, 400), (-140, 320)]
LONG_POSITIONS = [(-180, 320), (-180, 360), (-140, 320), (-100, 320)]
SHORT_POSITIONS = [(-180, 320), (-100, 360), (-140, 320), (-100, 320)]
CUBIC_LEFT_POSITIONS = [(-180, 360), (-180, 400), (-140, 360), (-140, 320)]
CUBIC_RIGHT_POSITIONS = [(-180, 320), (-180, 360), (-140, 400), (-140, 360)]


class AvailableFigures:
    def __init__(self):
        self.figure_list = []
        self.trash_list = []
        self.move_distance = 5
        self.create_figure()
        self.determine = 0

    def create_figure(self):
        square_list = []
        rectangle_list = []
        vertical_rectangle = []
        right_corner_list = []
        left_corner_list = []
        step_left_list = []
        step_right_list = []
        front_arrow_list = []
        back_arrow_list = []
        l_list = []
        r_list = []
        long_list = []
        short_list = []
        cubic_left_list = []
        cubic_right_list = []
        self.determine = randint(1, 15)
        if self.determine == 1:
            for position in SQUARE_POSITIONS:
                square_list.append(creation_code(position))
            self.figure_list.append(square_list)
        elif self.determine == 2:
            for place in H_RECTANGLE_POSITIONS:
                rectangle_list.append(creation_code(place))
            self.figure_list.append(rectangle_list)
        elif self.determine == 3:
            for locations in V_RECTANGLE_POSITIONS:
                vertical_rectangle.append(creation_code(locations))
            self.figure_list.append(vertical_rectangle)
        elif self.determine == 4:
            for locations in RIGHT_CORNER_POSITIONS:
                right_corner_list.append(creation_code(locations))
            self.figure_list.append(right_corner_list)
        elif self.determine == 5:
            for locations in LEFT_CORNER_POSITIONS:
                left_corner_list.append(creation_code(locations))
            self.figure_list.append(left_corner_list)
        elif self.determine == 6:
            for locations in STEP_LEFT_POSITIONS:
                step_left_list.append(creation_code(locations))
            self.figure_list.append(step_left_list)
        elif self.determine == 7:
            for locations in STEP_RIGHT_POSITIONS:
                step_right_list.append(creation_code(locations))
            self.figure_list.append(step_right_list)
        elif self.determine == 8:
            for locations in FRONT_ARROW_POSITIONS:
                front_arrow_list.append(creation_code(locations))
            self.figure_list.append(front_arrow_list)
        elif self.determine == 9:
            for locations in BACK_ARROW_POSITIONS:
                back_arrow_list.append(creation_code(locations))
            self.figure_list.append(back_arrow_list)
        elif self.determine == 10:
            for locations in L_POSITIONS:
                l_list.append(creation_code(locations))
            self.figure_list.append(l_list)
        elif self.determine == 11:
            for locations in R_POSITIONS:
                r_list.append(creation_code(locations))
            self.figure_list.append(r_list)
        elif self.determine == 12:
            for locations in LONG_POSITIONS:
                long_list.append(creation_code(locations))
            self.figure_list.append(long_list)
        elif self.determine == 13:
            for locations in SHORT_POSITIONS:
                short_list.append(creation_code(locations))
            self.figure_list.append(short_list)
        elif self.determine == 14:
            for locations in CUBIC_LEFT_POSITIONS:
                cubic_left_list.append(creation_code(locations))
            self.figure_list.append(cubic_left_list)
        elif self.determine == 15:
            for locations in CUBIC_RIGHT_POSITIONS:
                cubic_right_list.append(creation_code(locations))
            self.figure_list.append(cubic_right_list)

    def move_down(self):
        for item in self.figure_list[0]:
            item.setheading(270)
            item.forward(5)

    def move_left(self):
        if self.figure_list[0][0].xcor() > -180:
            for item in self.figure_list[0]:
                item.setheading(180)
                item.forward(40)
            self.move_down()

    def move_right(self):
        if self.figure_list[0][3].xcor() < 180:
            for item in self.figure_list[0]:
                item.setheading(0)
                item.forward(40)
            self.move_down()


# extra functionality:
def creation_code(coordinate):
    figure = Turtle()
    figure.shape("square")
    figure.shapesize(stretch_wid=2, stretch_len=2)
    figure.penup()
    figure.pencolor("maroon")
    figure.fillcolor("light green")
    figure.setposition(coordinate)
    return figure
