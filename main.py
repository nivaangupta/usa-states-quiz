import turtle
import pandas

game_is_on = True
s = 0
screen = turtle.Screen()
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
score = turtle.Turtle()
score.color('black')
score.hideturtle()
score.penup()
score.goto(300, 270)
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
State_List = data.state.tolist()
states = data.state.tolist()
x_list = data.x.tolist()
y_list = data.y.tolist()
correct = []
learn = {}

while s < 50:
    score.clear()
    score.write(f'{s}/50', False, align='center', font=('courier', 38, 'normal'))
    guess = screen.textinput(f"{s}/50 guessed", "Think of a U.S. state and type it here").title()

    for state in states:
        if guess == state:
            i = State_List.index(guess)
            x = x_list[i]
            y = y_list[i]
            writer.goto(x, y)
            writer.write(state, False, align='center', font=('courier', 18, 'normal'))
            correct.append(state)
            states.remove(state)
            s += 1
        if guess == 'Exit':
            learn = {
                'Yet to learn': states
            }
            df = pandas.DataFrame(learn)
            df.to_csv('homework.csv')
            s = 100


