from turtle import Turtle


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
