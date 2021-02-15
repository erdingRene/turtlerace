from turtle import Turtle, Screen
import random as rd

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Please enter the color: ")

colors = ("red", "orange", "yellow", "green", "blue", "purple")
turtles = []
for colour in colors:
    tim = Turtle(shape="turtle")
    tim.color(colour)
    turtles.append(tim)

x_coordinate = -200
y_coordinate = 200
for turtle in turtles:
    y_coordinate -= 50
    turtle.penup()
    turtle.goto(x=x_coordinate, y=y_coordinate)


def check_if_final_is_reached():
    for turtle in turtles:
        if turtle.xcor() >= 200:
            print(bet)
            if turtle.color()[0] == bet:
                screen.title("You won!")
            else:
                screen.title("You lost!")
            return True


final_reached = False
while not final_reached:
    for turtle in turtles:
        turtle.forward(rd.randint(1, 10))
        if check_if_final_is_reached():
            final_reached = True
            break

screen.exitonclick()
