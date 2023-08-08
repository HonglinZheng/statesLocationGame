from turtle import Turtle

FONT = ("Arial", 24, "normal")


class State(Turtle):
    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y

    def show_spot(self):
        self.shape("circle")
        self.hideturtle()
        self.color("blue")
        self.penup()
        self.goto(self.x, self.y)
        self.showturtle()

    def show_name(self):
        """
        this function shows state's name in blue to imply correct choice
        """
        self.hideturtle()
        self.penup()
        if self.name == "Connecticut":
            self.goto(self.x, self.y-10)
        else:
            self.goto(self.x, self.y)
        self.write(self.name, align="center", font=FONT)

    def show_ans(self):
        """
        this function shows state's name in red to imply wrong choice
        """
        self.hideturtle()
        self.color("red")
        self.penup()
        self.goto(self.x, self.y)
        self.write(self.name, align="center", font=FONT)