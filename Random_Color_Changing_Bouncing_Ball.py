"""
This application changes color randomly of a bouncing ball
"""


# importing libraries

from graphics import Canvas
import random
import time

# initialization of constant

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 450
BALL_DIAMETER = 25
INITIAL_VELOCITY = 5
START_X = 0
START_Y = 0
DELAY = 0.001

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    color = random_color()
    colors = ['blue', 'purple', 'salmon','magenta' 'lightblue', 'cyan', 'forestgreen', 'pink', 'red' ]

    # Declarizaion of variables

    x_velocity = INITIAL_VELOCITY
    y_velocity = INITIAL_VELOCITY
    ball_x = START_X
    ball_y = START_Y

    # Creating the ball with color
    ball = canvas.create_oval(ball_x, ball_y,
                              ball_x + BALL_DIAMETER,
                              ball_y + BALL_DIAMETER,
                              color)


    # Moving the bouncing ball

    while True:
        if (ball_x < 0) or (ball_x + BALL_DIAMETER >= CANVAS_WIDTH):
            x_velocity = -x_velocity
            canvas.set_color(ball, random.choice(colors))
        if (ball_y < 0) or (ball_y + BALL_DIAMETER >= CANVAS_HEIGHT):
            y_velocity = -y_velocity
            canvas.set_color(ball, random.choice(colors))
        ball_x += x_velocity
        ball_y += y_velocity
        canvas.moveto(ball, ball_x, ball_y)
        time.sleep(DELAY)


# Defination of custom random_color which can change the color of bouncing ball randomly
def random_color():
    colors = ['blue', 'purple', 'salmon','magenta' 'lightblue', 'cyan', 'forestgreen', 'pink', 'red' ]
    return random.choice(colors)


if __name__ == '__main__':
    main()
