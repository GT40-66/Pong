from turtle import Turtle


class GameManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.pendown()
        self.speed("fastest")
        self.pensize(5)
        while self.ycor() > -300:
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()




