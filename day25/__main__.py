import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
screen.tracer(0)

states = pandas.read_csv("50_states.csv")
correct_answers = []
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
running = True

while len(correct_answers) < 50:
    screen.update()
    answer = screen.textinput(f"{len(correct_answers)}/{len(states)} States Correct", "What's another state's name?")

    if answer is None:
        states_to_learn = states.query("state not in @correct_answers")
        states_to_learn.state.to_csv("learn.csv")
        break
    else:
        rows = states[states.state == answer.title()]
        if len(rows) > 0 and answer not in correct_answers:
            state = rows.state.iat[0]
            x = rows.x.iat[0]
            y = rows.y.iat[0]

            correct_answers.append(rows.state.iat[0])

            writer.goto(x, y)
            writer.write(f"{state}")
