# Simple Ping-pong in Python 3
# By Kabin Giri


import turtle
import winsound
import sys

wn = turtle.Screen()
wn.title("Ping-pong by Kabin Giri")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score

score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # 100 by 20
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # 100 by 20
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, 'normal'))


# Function

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


# Keyboard Binding


wn.listen()
wn.onkeypress(paddle_a_up, 'w')
wn.onkeypress(paddle_a_down, 's')
wn.onkeypress(paddle_b_up, 'Up')
wn.onkeypress(paddle_b_down, 'Down')

# Main game Loop

game_is_over = False


def game_over(winner):
    global game_is_over
    game_is_over = True
    pen.clear()
    pen.write(f"Game Over! {winner} wins!", align="center", font=("Courier", 24, 'normal'))
    pen.goto(0, -40)
    pen.write("Press 'P' to play again or 'Q' to quit", align="center", font=("Courier", 16, 'normal'))

    # Wait for user input to play again or quit
    wn.listen()
    wn.onkeypress(lambda: play_again(), 'p')
    wn.onkeypress(sys.exit, 'q')


def play_again():
    global score_a, score_b, game_is_over
    game_is_over = False
    score_a = 0
    score_b = 0
    pen.clear()
    pen.goto(0, 260)
    pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, 'normal'))
    paddle_a.goto(-350, 0)
    paddle_b.goto(350, 0)
    ball.goto(0, 260)
    ball.dx = 0.1
    ball.dy = 0.1
    start_game()


def start_game():
    global score_b, score_a, game_is_over
    welcome_pen.clear()
    while not game_is_over:
        wn.update()

        # Move the Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border Checking

        if ball.ycor() > 290:
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
            ball.sety(290)
            ball.dy *= -1  # reverses the direction of ball

        if ball.ycor() < -290:
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
            ball.sety(-290)
            ball.dy *= -1  # reverses the direction of ball

        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, 'normal'))

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center",
                      font=("Courier", 24, 'normal'))

        # Paddle and Ball collosion

        if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 45 > ball.ycor() > paddle_b.ycor() - 45):
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
            ball.setx(340)
            ball.dx *= -1

        if (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 45 > ball.ycor() > paddle_a.ycor() - 45):
            winsound.PlaySound('bounce.wav', winsound.SND_ASYNC)
            ball.setx(-340)
            ball.dx *= -1

        if score_a == 5:
            game_over("Player A")
        elif score_b == 5:
            game_over("Player B")


welcome_pen = turtle.Turtle()
welcome_pen.speed(0)
welcome_pen.color('white')
welcome_pen.penup()
welcome_pen.hideturtle()
welcome_pen.goto(0, 100)
welcome_pen.write("Welcome to Ping-Pong!\n By Kabin Giri", align="center", font=("Courier", 30, 'normal'))
welcome_pen.goto(0, 40)
welcome_pen.write("Player A: Use 'W' and 'S' keys to move", align="center", font=("Courier", 20, 'normal'))
welcome_pen.goto(0, 0)
welcome_pen.write("Player B: Use 'Up' and 'Down' arrow keys to move", align="center", font=("Courier", 20, 'normal'))
welcome_pen.goto(0, -60)
welcome_pen.write("Press any key to start the game!", align="center", font=("Courier", 24, 'normal'))

# Wait for a key press to start the game
wn.listen()
wn.onkeypress(start_game)

# Main game loop (start_game function will handle this)
turtle.done()
