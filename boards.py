from turtle import Turtle, Screen
screen = Screen()


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.left = None
        self.right = None

    def form_board(self, orientation):
        board = Turtle("square")
        board.color("white")
        board.penup()
        board.shapesize(stretch_wid=3, stretch_len=1)
        if orientation == "left":
            board.goto(-260, 0)
            self.left = board
        elif orientation == "right":
            board.goto(260, 0)
            self.right = board
        else:
            board.shapesize(stretch_wid=35, stretch_len=0.5)
            board.goto(0, 0)

    def left_moveup(self):
        if self.left.ycor() < 260:
            self.left.goto(-260, self.left.ycor()+20)

    def left_movedown(self):
        if self.left.ycor() > -260:
            self.left.goto(-260, self.left.ycor() - 20)

    def right_moveup(self):
        if self.right.ycor() < 260:
            self.right.goto(260, self.right.ycor() + 20)

    def right_movedown(self):
        if self.right.ycor() > -260:
            self.right.goto(260, self.right.ycor() - 20)

    def keys(self):
        screen.onkeypress(self.left_moveup, "w")
        screen.onkeypress(self.left_movedown, "s")
        screen.onkeypress(self.right_moveup, "Up")
        screen.onkeypress(self.right_movedown, "Down")
