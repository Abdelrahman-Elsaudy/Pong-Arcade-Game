from turtle import Turtle

BALL_STEP = 10
BALL_SHAPE = 0.8


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(BALL_SHAPE)
        self.penup()

    def move(self, main, second):
        self.setheading(main)
        self.forward(BALL_STEP)
        self.setheading(second)
        self.forward(BALL_STEP)
