import pygame as pg

class Bricks:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.colors = ['brown', 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        self.bricks = []
        self.brick_colors = []
        self.set_values()

    # Create brick objects
    def set_values(self):
        y_values = [int(y) for y in range(75, 400, 45)]
        x_values = [int(x) for x in range(20, 1440, 118)]
        y_index = 0
        self.loop(x_values, y_values, y_index)
    
    def loop(self, x_values, y_values, y_index):
        for n in x_values:
            if n == x_values[-1]:
                if y_index < len(y_values) - 1:
                    y_index += 1
                    self.loop(x_values, y_values, y_index)
            else:
                x = n
                y = y_values[y_index]
                brick = pg.Rect(x, y, self.width, self.height)
                self.bricks.append(brick)
                self.brick_colors.append(self.colors[y_index])
    
    def show_bricks(self):
        for loop in range(len(self.bricks)):
            brick = self.bricks[loop]

            # Brick color logic
            if brick.y == 75:
                color = self.colors[0]
            if brick.y == 120:
                color = self.colors[1]
            if brick.y == 165:
                color = self.colors[2]
            if brick.y == 210:
                color = self.colors[3]
            if brick.y == 255:
                color = self.colors[4]
            if brick.y == 300:
                color = self.colors[5]
            if brick.y == 345:
                color = self.colors[6]
            if brick.y == 390:
                color = self.colors[7]

            pg.draw.rect(self.screen, color, brick)

    # Check for collision with ball
    def update(self, ball, score):
        for brick in self.bricks:
            if brick.collidepoint(ball.x, ball.y - ball.radius) or brick.collidepoint(ball.x, ball.y + ball.radius):
                self.bricks.remove(brick)
                ball.bounce_y()
                score.score += 500
