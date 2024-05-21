from turtle import Screen
from game_manager import GameManager
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Air Hockey")
screen.tracer(0)

gm = GameManager()
ball = Ball()
score_board_l = Score((-50, 270))
score_board_r = Score((50, 270))

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.ball_movement()
    time.sleep(ball.move_speed)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() == -330 or ball.distance(r_paddle) < 50 and ball.xcor() == 330:
        ball.bounce_x()

    # Detect out of bounds
    if ball.xcor() > 390:
        score_board_l.increase_score()
        time.sleep(0.5)
        ball.refresh((-100, 0))

    if ball.xcor() < -390:
        score_board_r.increase_score()
        time.sleep(0.5)
        ball.refresh((100, 0))

screen.exitonclick()
