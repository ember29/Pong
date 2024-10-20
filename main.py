from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)





r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()






screen.listen()
screen.onkey(fun=r_paddle.up,key="Up")
screen.onkey(fun=r_paddle.down,key="Down")
screen.onkey(fun=l_paddle.l_down,key="s")
screen.onkey(fun=l_paddle.l_up,key="w")


"""not use the function with ()"""
is_game_on=True
while is_game_on:
    time.sleep(ball.speed_move)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:

        ball.bounce_y()

    if (ball.xcor() > 320 and ball.distance(r_paddle) <50) or (ball.xcor() < -320 and ball.distance(l_paddle) <50):
        ball.bounce_x()
    #right paddle missing
    if ball.xcor() > 380 :
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()












screen.exitonclick()
