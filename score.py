from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.value = 0

    def display_left(self):
        self.goto(-70, 220)
        self.write(self.value, False, "right",  font=('Arial', 30, 'normal'))

    def display_right(self):
        self.goto(70, 220)
        self.write(self.value, False, "right",  font=('Arial', 30, 'normal'))

    def score_right(self):
        self.clear()
        self.value += 1

    def score_left(self):
        self.clear()
        self.value += 1
