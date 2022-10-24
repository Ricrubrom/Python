import turtle
import winsound

wn = turtle.Screen()  # Creating window
wn.title('Pong')  # Title
wn.bgcolor('black')  # Bg color
wn.setup(width=800, height=600)  # Dimensions
wn.tracer(0)  # Stops the window from updating, we have to update it manually

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)  # Speed of animation
paddle_a.shape("square")
paddle_a.color('white')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)  # Speed of animation
paddle_b.shape("square")
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)  # Speed of animation
ball.shape("square")
ball.color('white')
ball.penup()    # Doesn't leave a trace behind as it moves
ball.goto(0, 0)
ball.dx = 1/6
ball.dy = 1/6

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align='center',
          font=('Courier', 24, 'normal'))


# Movement


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')


# Game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border checking
    if ball.ycor() > 290:  # Top border
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound(
            'F:\Archivos de Programa\Cosas\Coding\Python\Games\Game 1 - Pong\Wall.wav', winsound.SND_ASYNC)
    if ball.ycor() < -290:  # Bottom border
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound(
            'F:\Archivos de Programa\Cosas\Coding\Python\Games\Game 1 - Pong\Wall.wav', winsound.SND_ASYNC)

    if ball.xcor() > 390:  # Left side wins
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        winsound.PlaySound(
            'F:\Archivos de Programa\Cosas\Coding\Python\Games\Game 1 - Pong\Score.wav', winsound.SND_ASYNC)
        pen.clear()
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center',
                  font=('Courier', 24, 'normal'))

    if ball.xcor() < -390:  # Right side wins
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        winsound.PlaySound(
            'F:\Archivos de Programa\Cosas\Coding\Python\Games\Game 1 - Pong\Score.wav', winsound.SND_ASYNC)
        pen.write(f"Player A: {score_a}  Player B: {score_b}", align='center',
                  font=('Courier', 24, 'normal'))

    if paddle_a.ycor()+40 > 290:
        paddle_a.sety(250)

    if paddle_a.ycor()-40 < -290:
        paddle_a.sety(-250)

    if paddle_b.ycor()+40 > 290:
        paddle_b.sety(250)

    if paddle_b.ycor()-40 < -290:
        paddle_b.sety(-250)

    # Paddle and ball collision
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):  # Left Paddle
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound(
            'F:\Archivos de Programa\Cosas\Coding\Python\Games\Game 1 - Pong\Paddle.wav', winsound.SND_ASYNC)
        ball.dx *= 1.03
        ball.dy *= 1.03
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):  # Right Paddle
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound(
            'F:\Archivos de Programa\Cosas\Coding\Python\Games\Game 1 - Pong\Paddle.wav', winsound.SND_ASYNC)
        ball.dx *= 1.03
        ball.dy *= 1.03
