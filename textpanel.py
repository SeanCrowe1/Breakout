import pygame as pg
from values import *

class TextPanel:
    def __init__(self, x, color, screen):
        self.screen = screen
        self.color = color
        self.x = x
        self.fail = False
        self.win = False
        self.close = False
        self.score = 0
        self.high_score = 0
        self.lives = 5
        self.font = SCORE_FONT
        self.score_font = pg.font.SysFont(self.font, 20)

    # Creates scoreboard text in corner of screen
    def show_scores(self):
        score_text = self.score_font.render(f"Score:       {self.score}", True, self.color)
        high_score_text = self.score_font.render(f"High Score:  {self.high_score}", True, self.color)
        lives_text = self.score_font.render(f"Lives:      x0{self.lives}", True, self.color)

        self.screen.blit(score_text, (self.x, 10))
        self.screen.blit(high_score_text, (self.x, 26))
        self.screen.blit(lives_text, (self.x, 42))

    # Checks for game end conditions
    def update(self, bricks, paddle, screen):
        if self.is_game_over():
            self.game_over(paddle, screen)
        elif len(bricks.bricks) == 0:
            self.success(paddle, screen)

    def is_game_over(self):
        if self.lives == 0:
            return True
        return False
    
    # Game end sequences
    def game_over(self, paddle, screen):
        pg.time.delay(100)
        screen.fill(BG_COLOR)
        paddle.draw(screen)
        self.show_scores()
        game_over_color = 'red'
        game_over_font = pg.font.SysFont(self.font, 30, True)
        game_over_text = game_over_font.render(f"Game Over! Press 'R' to restart.", True, game_over_color)
        self.screen.blit(game_over_text, (450, 300))
        self.record_high_score()
        self.fail = True

    def success(self, paddle, screen):
        pg.time.delay(100)
        screen.fill(BG_COLOR)
        paddle.draw(screen)
        self.show_scores()
        game_success_color = 'green'
        game_success_font = pg.font.SysFont(self.font, 30, True)
        game_success_text = game_success_font.render(f"You won! Press 'R' to restart.", True, game_success_color)
        self.screen.blit(game_success_text, (450, 300))
        self.record_high_score()
        self.win = True

    # High score logic
    def set_high_score(self):
        try:
            with open("records.txt", mode="r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            with open("records.txt", mode="w") as data:
                data.write("0")
                score = 0
        else:
            score = lines[0]

        self.high_score = int(score)

    def record_high_score(self):
        if self.score > self.high_score:
            with open("records.txt", mode="w") as file:
                file.write(f"{self.score}")

    # Reset countdown animation
    def reset_countdown(self, reset, reset_x):
        while reset > 0:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.close = True
                    pg.quit()
                    return
            countdown_color = 'white'
            countdown_font = pg.font.SysFont(self.font, 40, True)
            countdown_text = countdown_font.render(f"{reset}!", True, countdown_color)
            self.screen.blit(countdown_text, (reset_x, 600))
            pg.display.flip()
            reset -= 1
            reset_x += 50
            pg.time.delay(500)