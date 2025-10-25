import pygame as pg
from values import *

class Ball:
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.radius = BALL_RADIUS
        self.color = pg.Color(BALL_COLOR)
        self.x_speed = BALL_X_SPEED
        self.y_speed = BALL_Y_SPEED

    def update(self, bricks, clock, paddle, score, screen):
        # Movement logic
        self.draw()

        # Collision check logic
        self.collision_check(bricks, clock, paddle, score, screen)
        self.paddle_collision_check(paddle, score)

    def draw(self):
        pg.draw.circle(self.screen, self.color, [self.x, self.y], self.radius)
        self.y -= self.y_speed
        self.x -= self.x_speed    
        
    def bounce_x(self):
        self.x_speed *= -1

    def bounce_y(self):
        self.y_speed *= -1

    def collision_check(self, bricks, clock, paddle, score, screen):
        if self.x - self.radius <= 0 or self.x + self.radius >= self.screen.get_width():
            self.bounce_x()
        if self.y + self.radius <= 10:
            self.bounce_y()
        if self.y + self.radius >= 870:
            self.reset(bricks, clock, paddle, score, screen)
            

    def paddle_collision_check(self, paddle, score):
        if (paddle.rect.y < self.y + self.radius < paddle.rect.y + paddle.height
                and
            paddle.rect.x < self.x + self.radius < paddle.rect.x + paddle.width):
            self.bounce_y()
            self.y = paddle.y - self.radius
            score.score += 10

    # Game reset logic
    def reset(self, bricks, clock, paddle, score, screen):
        # Check what type of reset is done
        score.lives -= 1
        if score.lives == 0:
            score.game_over(paddle, screen)
        if score.score > 1000:
            score.score -= 1000
        else:
            score.score -= score.score
        pg.time.delay(250)

        # Play reset animations
        paddle.reset_position(self, bricks, clock, score, screen)
        pg.time.delay(500)

        # Make sure ball is moving upwards after reset
        if self.y_speed < 0:
            self.bounce_y()

        # Check if countdown should play
        if score.fail == False and score.win == False:
            score.reset_countdown(3, 655)