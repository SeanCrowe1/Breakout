import pygame as pg
from values import *

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.color = pg.Color("white")

    def draw(self, screen):
        pg.draw.rect(screen, self.color, self.rect)

    # Movement check
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.move_right()
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.move_left()

    def move_right(self):
        if self.rect.x + self.width <= 1440:
            self.rect.x += PADDLE_SPEED

    def move_left(self):
        if self.rect.x >= 0:
            self.rect.x -= PADDLE_SPEED

    # Reset animation logic
    def reset_position(self, ball, bricks, clock, score, screen):
        # Sets values for visible objects during animation
        ball.x = 1500
        ball.y = 1000
        ball.draw()
        screen.fill(BG_COLOR)
        self.draw(screen)
        bricks.show_bricks()
        score.show_scores()
        pg.display.flip()
        
        # Animation loop
        while self.rect.x != 670:
            if self.rect.x > 670:
                self.move_left()
            else:
                self.move_right()
            screen.fill(BG_COLOR)
            self.draw(screen)
            bricks.show_bricks()
            score.show_scores()
            pg.display.flip()
            clock.tick(60)
        
        # Reset ball for continued gameplay
        ball.x = 716
        ball.y = self.y - ball.radius * 4
        ball.draw()
