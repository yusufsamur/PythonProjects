import turtle
import winsound

wn = turtle.Screen()
wn.title("3000 dolar maas alcam")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score

score_1 = 0
score_2 = 0

# Paddle 1

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player 1: 0 | Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Functions

def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)


# Keyboard Binding
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

# Main game loop
winsound.PlaySound("bgMusic.wav", winsound.SND_ASYNC | winsound.SND_LOOP)
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1

        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center",
                  font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1

        pen.clear()
        pen.write("Player 1: {} | Player 2: {}".format(score_1, score_2), align="center",
                  font=("Courier", 24, "normal"))

    # paddle and ball collisions

    if (ball.xcor() > 330 and ball.xcor() < 340) and (
            ball.ycor() > paddle_2.ycor() - 50 and ball.ycor() < paddle_2.ycor() + 50):
        ball.setx(330)
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -340) and (
            ball.ycor() > paddle_1.ycor() - 50 and ball.ycor() < paddle_1.ycor() + 50):
        ball.setx(-330)
        ball.dx *= -1
