# Simple Pong game in Python 3

import turtle

# CONSTANTS
wn = turtle.Screen()
wn.title("Pong game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Initial values of scoreboard
score_a = 0
score_b = 0

# Set up left side paddle
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Set up right side paddle
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Set up ball
ball = turtle.Turtle()
ball.speed(0)  # speed of animation
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = -0.15

# Display scoreboard
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions

# Move left paddle up
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


# Move left paddle down
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


# Move right paddle up
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


# Move Right paddle down
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for ball
    # Bounce ball from top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    # Bounce ball from bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # If ball goes past right paddle, player A scores point
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # If ball goes past left paddle, player B scores point
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # Paddle border checking
    if paddle_a.ycor() > 250:
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)

    if paddle_b.ycor() > 250:
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # Paddle and ball collisions
    if ball.xcor() > 330 and (ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(330)
        ball.dx *= -1

    if ball.xcor() < -330 and (ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-330)
        ball.dx *= -1
