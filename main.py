import pygame as pg
from ball import Ball
from bricks import Bricks
from paddle import Paddle
from textpanel import TextPanel
from values import *


def main():
    # Initialisation settings
    pg.init()

    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Breakout Game")
    clock = pg.time.Clock()

    # Objects
    ball = Ball(BALL_X, BALL_Y, screen)
    bricks = Bricks(screen, BRICK_WIDTH, BRICK_HEIGHT)
    paddle = Paddle(PADDLE_X, PADDLE_Y)
    score = TextPanel(SCORE_X, SCORE_COLOR, screen)
    score.set_high_score()

    # Game Loop
    while True:
        # Check for quitting game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            
        # Check for resetting game
        reset_check(ball, bricks, clock, paddle, score, screen)

        # Check for game over
        if score.fail == True:
            if score.lives > 0:
                score.fail = False
            continue
        if score.win == True:
            continue

        # Draw new frame
        update_screen(bricks, paddle, score, screen)
        
        # Update values for next frame
        paddle.update()
        ball.update(bricks, clock, paddle, score, screen)
        bricks.update(ball, score)
        score.update(bricks, paddle, screen)
        
        # Second check for quitting game
        if score.close == True:
            return
        
        # Refresh screen and control frame rate
        pg.display.flip()
        clock.tick(60)
    
# Added delays for smoother reset animation
def reset_check(ball, bricks, clock, paddle, score, screen):
    keys = pg.key.get_pressed()
    if keys[pg.K_r]:
        pg.time.delay(250)
        score.score = 0
        score.set_high_score()
        update_screen(bricks, paddle, score, screen)
        pg.display.flip()
        pg.time.delay(250)
        score.lives = 5
        score.fail = False
        score.win = False
        update_screen(bricks, paddle, score, screen)
        pg.display.flip()
        pg.time.delay(250)
        bricks.bricks.clear()
        bricks.set_values()
        update_screen(bricks, paddle, score, screen)
        pg.display.flip()
        pg.time.delay(250)
        score.lives = 6
        ball.reset(bricks, clock, paddle, score, screen)

# Used for repeated update calls
def update_screen(bricks, paddle, score, screen):
    screen.fill(BG_COLOR)
    paddle.draw(screen)
    bricks.show_bricks()
    score.show_scores()

# Runs main() function when file called in terminal
if __name__ == "__main__":
    main()