from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color("white")
        self.player_one_score = 0
        self.player_two_score = 0
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 320)
        self.write(self.player_one_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 320)
        self.write(self.player_two_score, align=ALIGNMENT, font=FONT)

    def add_score_player_one(self):
        self.player_one_score += 1
        self.update_scoreboard()

    def add_score_player_two(self):
        self.player_two_score += 1
        self.update_scoreboard()

    