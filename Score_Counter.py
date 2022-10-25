from turtle import Turtle


class Tracker(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(300, 300)
        self.current_score = 0

    def write_score(self):
        self.color("old lace")
        self.setposition(180, 265)
        self.clear()
        self.write(f"Score: {self.current_score}", align="right", font=("Courier", 18, "bold"))

    def game_over(self):
        self.color("black")
        self.setposition(0, 200)
        self.write(f"GAME OVER", align="center", font=("Courier", 22, "bold"))
