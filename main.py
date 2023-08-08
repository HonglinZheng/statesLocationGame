import turtle
import scoreboard
import pandas as pd
from state import State
import random

global CURRENT
global CLOSEDIS
global SCORE

CLOSEDIS = 10
SCORE = 0

# canvas setup
screen = turtle.Screen()
screen.setup(width=1250, height=1000)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
scoreboard = scoreboard.Scoreboard()


# list setup
df = pd.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed = []
states_dict = {}
# dot setup
for index, row in df.iterrows():
    state = State(row.state, int(row.x), int(row.y))
    state.show_spot()
    states_dict[row.state] = state


def check_ans(x, y):
    """
    this function interacts with user to imply whether user has clicked at correct spot
    wherever user clicks, answer will show in the correct place
    red text means wrong answer
    blue text means correct answer
    :param x: x coordinate of click
    :param y: y coordinate of click
    """
    global all_states, guessed, df, CURRENT, states_dict, SCORE
    state_data = df[df.state == CURRENT]
    the_state = states_dict[CURRENT]
    target_x = int(state_data.x)
    target_y = int(state_data.y)
    guessed.append(CURRENT)  # memorize what have been answered
    all_states.remove(CURRENT)  # update the to-do list
    if target_x-CLOSEDIS < x < target_x+CLOSEDIS and target_y-CLOSEDIS < y < target_y+CLOSEDIS:
        # correct spot
        SCORE += 1
        the_state.show_name()
    else:
        # wrong spot
        the_state.show_ans()

    if len(guessed) <= 50:  # generate the next target
        thenext = random.choice(all_states)
        CURRENT = thenext
        scoreboard.prompt(CURRENT)
    else:  # have finished all states; need to end the game
        scoreboard.end(SCORE)


global CURRENT
CURRENT = random.choice(all_states)  # choose the first state
guessed.append(CURRENT)
scoreboard.prompt(CURRENT)

screen.listen()
turtle.onscreenclick(check_ans)  # waiting for click to check answer
turtle.mainloop()