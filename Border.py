from turtle import Turtle


class SideBorder(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.pencolor("light gray")
        self.fillcolor("peru")
        self.hideturtle()
        self.penup()

    def draw_borders(self):
        # left side:
        self.setposition(-220, 280)
        self.setheading(270)
        self.stamp()
        for i in range(14):
            self.forward(40)
            self.stamp()
        # right side:
        self.setposition(220, 280)
        self.setheading(270)
        self.stamp()
        for i in range(14):
            self.forward(40)
            self.stamp()


class BottomBorder:
    def __init__(self):
        self.bottom_list = []
        self.x_start = -180
        self.y_start = -280
        self.create_shape()

    def create_shape(self):
        for repeat in range(10):
            floor = Turtle()
            floor.shape("square")
            floor.shapesize()
            floor.shapesize(stretch_wid=2, stretch_len=2)
            floor.pencolor("light gray")
            floor.fillcolor("peru")
            floor.hideturtle()
            floor.penup()
            self.bottom_list.append(floor)

    def deploy_floor(self):
        for item in self.bottom_list:
            item.setposition(self.x_start, self.y_start)
            item.stamp()
            self.x_start += 40


class GridLines(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.pencolor("dim grey")
        # extra variable:
        self.x_position = -160
        self.y_position = 260

    def draw_verticals(self):
        for again in range(9):
            self.setposition(self.x_position, 300)
            self.setheading(270)
            self.pendown()
            for repeat in range(14):
                self.forward(40)
            self.penup()
            self.x_position += 40

    def draw_horizontals(self):
        for rerun in range(13):
            self.setposition(-200, self.y_position)
            self.setheading(0)
            self.pendown()
            for run in range(10):
                self.forward(40)
            self.penup()
            self.y_position -= 40


class CrossLine(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.pencolor("dark slate gray")
        self.fillcolor("indian red")
        self.setposition(300, 300)

    def draw_sign(self):
        self.setposition(-220, 160)
        self.stamp()
        self.setposition(220, 160)
        self.stamp()
