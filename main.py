from time import sleep
from turtle import Screen
from score import ScoreBoard
from ball import Ball
from players import Player
from net_circle import Net, Circle

player_one = Player()
player_two = Player()
player_one.goto(-580, 0)
player_two.goto(580, 0)

ball = Ball()

score_board = ScoreBoard()

net = Net()
circle= Circle()

# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1280, height=860)
screen.title("Pong Ping")

screen.tracer(0)

# Object move

screen.listen()
screen.onkey(player_one.go_up, "w")
screen.onkey(player_one.go_down, "s")
screen.onkey(player_two.go_up, "Up")
screen.onkey(player_two.go_down, "Down")

# Drawing the net

sleep(0.5)

net.move_forward()

# Game
game_on = True
while game_on:
    screen.update()
    ball.move()
    # print(player_one.xcor(), player_one.ycor())

    # Collision with upper and lower walls

    if abs(ball.ycor()) > 413:
        ball.bounce_y()

    if ball.xcor() > 660:
        score_board.add_score_player_one()
        ball.reset_position()

    if ball.xcor() < -660:
        score_board.add_score_player_two()
        ball.reset_position()

    # Collision with paddle
    if ball.distance(player_two) < 47:
        ball.bounce_x()

    if ball.distance(player_one) < 47:
        ball.bounce_x()

screen.exitonclick()
