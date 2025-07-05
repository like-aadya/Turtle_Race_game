import turtle
import random

screen = turtle.Screen()
screen.title("Turtle Race Game")
screen.bgcolor("skyblue")
screen.setup(width = 800, height = 600)

finish_line = 300
line = turtle.Turtle()
line.penup()
line.goto(finish_line, 250)
line.right(90)
line.pendown()
line.forward(500)
line.hideturtle()

colors = ["red", "blue", "green", "orange", "purple"]
y_positions = [-100, -50, 0, 50, 100]
all_turtles = []

for i in range(5):
    racer = turtle.Turtle(shape="turtle")
    racer.color(colors[i])
    racer.penup()
    racer.goto(x=-350, y=y_positions[i])
    all_turtles.append(racer)

    race_on = True

while race_on:
    for racer in all_turtles:
        move = random.randint(1, 10)
        racer.forward(move)

        # Check if turtle crossed the finish line
        if racer.xcor() >= finish_line:
            race_on = False
            winner_color = racer.color()[0]
            print(f"The winner is the {winner_color} turtle!")
            break

screen.exitonclick()