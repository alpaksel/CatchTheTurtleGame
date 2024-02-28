import time
import turtle

turtle_instance = turtle.Turtle()
turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light blue")
turtle_screen.title("Catch The Turtle")



countdown_time = 5

for i in range(countdown_time, 0, -1):
    turtle_instance.clear()
    turtle_instance.penup()
    turtle_instance.goto(0, 275)
    turtle_instance.write(str(i), font=("Arial", 24, "normal"))
    time.sleep(1)

turtle_instance.clear()
turtle_instance.write("Game Over!",align="center", font=("Arial", 24, "normal"))

time.sleep(1)

turtle.mainloop()