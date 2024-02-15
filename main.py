# Press "w" and "s" to move the left board up and down
# Press "Up" and "Down" to move the right board up and down

from turtle import Screen
from boards import Board
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)

board = Board()
board.form_board("left")
board.form_board("right")
board.form_board("net")
board.keys()

game_ball = Ball()
main = 90
second = 0

scoring_left = Score()
scoring_right = Score()

game_on = True
while game_on:
    screen.update()
    scoring_left.display_left()
    scoring_right.display_right()
    game_ball.move(main, second)
    time.sleep(0.02)

    if game_ball.ycor() >= 270:               # hitting borders changes the up/down direction but keeps the east/west.
        main = 270
    elif game_ball.ycor() <= -270:
        main = 90

    if game_ball.distance(board.right) < 30:   # hitting the boards keeps the up/down direction but changes east/west
        second = game_ball.heading() + 180
    elif game_ball.distance(board.left) < 30:
        second = game_ball.heading() - 180

    if game_ball.xcor() >= 280:
        scoring_left.score_left()
        game_ball.goto(0, 0)
        main = 90
        second = 180
    elif game_ball.xcor() <= -280:
        scoring_right.score_right()
        game_ball.goto(0, 0)
        main = 90
        second = 0

screen.exitonclick()
