import turtle
import random
import time

speed = 10
random1 = 350
random2 = 450
score = 0

screen = turtle.Screen()
screen.title("Flappy Turtle")
screen.setup(1.0, 1.0)
screen.bgcolor("pale turquoise")

flappy = turtle.Turtle()
top_pipe1 = turtle.Turtle()
bottom_pipe1 = turtle.Turtle()
top_pipe2 = turtle.Turtle()
bottom_pipe2 = turtle.Turtle()
top_pipe3 = turtle.Turtle()
bottom_pipe3 = turtle.Turtle()
build = turtle.Turtle()
scoreboard = turtle.Turtle()

flappy.hideturtle()
top_pipe1.hideturtle()
bottom_pipe1.hideturtle()
top_pipe2.hideturtle()
bottom_pipe2.hideturtle()
top_pipe3.hideturtle()
bottom_pipe3.hideturtle()
build.hideturtle()
scoreboard.hideturtle()


def reset():
   flappy.hideturtle()
   top_pipe1.hideturtle()
   bottom_pipe1.hideturtle()
   top_pipe2.hideturtle()
   bottom_pipe2.hideturtle()
   top_pipe3.hideturtle()
   bottom_pipe3.hideturtle()

   flappy.shape("turtle")
   flappy.color("gold")
   flappy.shapesize(2.5, 2.5)
   flappy.penup()
   flappy.goto(-400, 0)

   top_pipe1.shape("square")
   top_pipe1.color("lime green")
   top_pipe1.shapesize(30, 5)
   top_pipe1.penup()
   top_pipe1.goto(350, random.randint(random1, random2))

   bottom_pipe1.shape("square")
   bottom_pipe1.color("lime green")
   bottom_pipe1.shapesize(random.randint(25, 30), 5)
   bottom_pipe1.penup()
   bottom_pipe1.goto(350, -1 * random.randint(random1, random2))

   top_pipe2.shape("square")
   top_pipe2.color("lime green")
   top_pipe2.shapesize(random.randint(25, 30), 5)
   top_pipe2.penup()
   top_pipe2.goto(850, random.randint(random1, random2))

   bottom_pipe2.shape("square")
   bottom_pipe2.color("lime green")
   bottom_pipe2.shapesize(random.randint(25, 30), 5)
   bottom_pipe2.penup()
   bottom_pipe2.goto(850, -1 * random.randint(random1, random2))

   top_pipe3.shape("square")
   top_pipe3.color("lime green")
   top_pipe3.shapesize(random.randint(25, 30), 5)
   top_pipe3.penup()
   top_pipe3.goto(1350, random.randint(random1, random2))

   bottom_pipe3.shape("square")
   bottom_pipe3.color("lime green")
   bottom_pipe3.shapesize(random.randint(25, 30), 5)
   bottom_pipe3.penup()
   bottom_pipe3.goto(1350, -1 * random.randint(random1, random2))

   scoreboard.penup()
   scoreboard.color("white")
   scoreboard.write(score, font=("Arial", 40, "bold"), align="center")

   top_pipe1.showturtle()
   bottom_pipe1.showturtle()
   top_pipe2.showturtle()
   bottom_pipe2.showturtle()
   top_pipe3.showturtle()
   bottom_pipe3.showturtle()
   flappy.showturtle()


reset()


def draw(color):
   build.penup()
   build.color("medium turquoise")
   build.fillcolor(color)
   x = build.xcor()

   build.goto(-620, -300)
   build.begin_fill()
   build.goto(-570, -300)

   for i in range(5):
      build.sety(random.randint(10, 200))
      build.setx(x + 50)
      build.sety(random.randint(-100, -50))
      build.setx(x + 50)

   build.sety(-450)
   build.setx(-620)
   build.sety(0)

   build.end_fill()


def boing():
   y = flappy.ycor()
   flappy.sety(y + 60)


def gravity():
   y = flappy.ycor()
   flappy.sety(y - 5)


def movepipes():
   global speed

   x = top_pipe1.xcor()
   top_pipe1.setx(x - speed)
   x = top_pipe2.xcor()
   top_pipe2.setx(x - speed)
   x = top_pipe3.xcor()
   top_pipe3.setx(x - speed)

   x = bottom_pipe1.xcor()
   bottom_pipe1.setx(x - speed)
   x = bottom_pipe2.xcor()
   bottom_pipe2.setx(x - speed)
   x = bottom_pipe3.xcor()
   bottom_pipe3.setx(x - speed)


def pipeout(top, bottom):
   if top.xcor() <= -500:
      top.hideturtle()
      bottom.hideturtle()
      top.goto(1000, random.randint(random1, random2))
      bottom.goto(1000, -1 * random.randint(random1, random2))
      top.showturtle()
      bottom.showturtle()


screen.listen()
screen.onkeypress(boing, "space")


def collisions(top_pipe, bottom_pipe):
   y = flappy.ycor()
   if top_pipe.xcor() < -310 and top_pipe.xcor(
   ) > -490 and y > top_pipe.ycor() - 310:
      time.sleep(1)
      while flappy.ycor() > -375:
         flappy.sety(flappy.ycor() - 8)
      reset()

   if bottom_pipe.xcor() < -310 and bottom_pipe.xcor(
   ) > -490 and y < bottom_pipe.ycor() + 310:
      time.sleep(1)
      while flappy.ycor() > -375:
         flappy.sety(flappy.ycor() - 8)
      reset()


draw("medium turquoise")

while (True):
   gravity()
   movepipes()
   pipeout(top_pipe1, bottom_pipe1)
   pipeout(top_pipe2, bottom_pipe2)
   pipeout(top_pipe3, bottom_pipe3)
   collisions(top_pipe1, bottom_pipe1)
   collisions(top_pipe2, bottom_pipe2)
   collisions(top_pipe3, bottom_pipe3)

screen.mainloop()
