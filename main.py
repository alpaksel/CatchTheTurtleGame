import time
import turtle
import random


turtle_instance = turtle.Turtle()
turtle_instance_time = turtle.Turtle()
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")


def shape():
    turtle_instance.shape("turtle")
    turtle_instance.penup()
    turtle_instance.shapesize()
    turtle_instance.shapesize(stretch_wid=2, stretch_len=2)
    turtle_instance.color("green")
    random_x = random.randint(-400, 400)
    random_y = random.randint(-400, 400)
    turtle_instance.goto(random_x, random_y)


def timer():
    countdown_time = 10

    for i in range(countdown_time, 0, -1):
        turtle_instance_time.hideturtle()
        turtle_instance_time.clear()
        turtle_instance_time.penup()
        turtle_instance_time.goto(0, 275)
        turtle_instance_time.write(str(i), font=("Arial", 24, "normal"))
        time.sleep(1)

    turtle_instance_time.clear()
    turtle_instance_time.write("Game Over!",align="center", font=("Arial", 24, "normal"))


    time.sleep(1)

shape()
timer()

turtle.mainloop()