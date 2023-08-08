from turtle import Turtle
FONT = ("Arial", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.write_text(0, 418, "Welcome to this US states location game! Please wait for next prompt")

    def write_text(self, x, y, text):
        self.hideturtle()
        self.penup()
        self.goto(x, y)
        self.write(text, align="center", font=FONT)

    def prompt(self, state):
        self.clear()
        self.write_text(0, 418, f"Please click {state}")

    def end(self, score):
        self.clear()
        self.write_text(0, 418, f"Game over! score: {score}/50")

