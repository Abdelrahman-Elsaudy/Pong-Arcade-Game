# Pong The Arcade Game

---

- The famous multi-player game in which two opposite boards are bouncing a ball between them to score goals.

![pong_screenshot](https://github.com/Abdelrahman-Elsaudy/Pong-Arcade-Game/assets/158151388/f4f0b2e1-aa7b-4df1-a66d-2f2468a64bb2)
---

## Applied Skills:

---

**1. Object-Oriented Programming**

Dividing the project into:
- `ball.py` which creates the ball and moves it diagonally, this movement is determined by main direction (north/south) and secondary direction (east/west)
```
    def move(self, main, second):
        self.setheading(main)
        self.forward(BALL_STEP)
        self.setheading(second)
        self.forward(BALL_STEP)
```
- `boards.py` which creates the right and left boards, locates them and moves them. I used it also to create the net in the middle.
- `score.py` which displays and calculates both scores.
- `main.py` on which all of the above is called, the screen is set and the game_on loop works.


**2. Game Concept**

- The screen is updated inside a while loop on `main.py`, and each time it's updated the ball moves diagonally.
- At the beginning the ball moves in the north-east direction, and when a player scores, the ball moves to the north but in the opponent direction.
- When the ball hits up or down borders it changes its main direction (up/down) but keeps its secondary direction (east/west).
```
    if game_ball.ycor() >= 270:      # Hitting the top border.
        main = 270                   # Moving to the south.
    
    elif game_ball.ycor() <= -270:   # Hitting the down border.
        main = 90                    # Moving to the north.
```

- When the ball hits right or left boards it changes its secondary direction (east/west) but keeps its main direction (up/down).
```    
    if game_ball.distance(board.right) < 30:   # Hitting the right board.
        second = 180                           # Moving to the west.

    elif game_ball.distance(board.left) < 30:  # Hitting the left board.
        second = 0                             # Moving to the east.
```
- When the ball passes right board net, the left board scores.
```    
    if game_ball.xcor() >= 280:
        scoring_left.score_left()
        game_ball.goto(0, 0)
        main = 90
        second = 180
```
- When the ball passes left board net, the right board scores.
```    
    elif game_ball.xcor() <= -280:
        scoring_right.score_right()
        game_ball.goto(0, 0)
        main = 90
        second = 0
```

---
## To be Improved:
- When a player presses on a button continuously, the other player can't do the same.
- When the ball touches the edge of either the right or the left boards, it circulates around it for an instance before bouncing back normally.

---

_Credits to: 100-Days of Code Course on Udemy._