import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S Sate game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
position_x = data["x"].to_list()
position_y = data["y"].to_list()
print(position_x)

x = 0
while x <= 50:
    answer = screen.textinput(f"{x}/50 States guessed", "Guess a State").lower()

    variable = 0
    turtles = []
    guessed = []

    for state in states:

        if answer == state.lower() and answer not in guessed:
            new_turtle = turtle.Turtle()
            new_turtle.penup()
            new_turtle.hideturtle()
            new_x = position_x[variable]
            new_y = position_y[variable]
            new_turtle.goto(new_x, new_y)
            new_turtle.write(answer, False, "center", font=("Arial", 8, "normal"))
            print("right")
            print(new_x)
            variable = - 1
            x += 1
            guessed.append(answer)
        else:
            pass

        variable += 1


screen.exitonclick()