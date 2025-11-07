# Galaxy
# By Jerry Bai

import turtle
import random
import math

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 800
BACKGROUND = "Black"  # The dark space
COLORS = [
    "Yellow",
    "Orange",
    "Blue",
    "Red",
    "Spring Green",
    "Purple",
    "Cyan",
    "Magenta",
    "White",
]  # star and arm colors
NUM_ARMS = 5  # number of main spiral arms
START_LEVEL = 4  # recursion depth (the expert requirement in the pdf)
START_LENGTH = 260  # how long each main arm is
STEP_ANGLE = 18  # how sharply the arm turns every step
STEPS_PER_ARM = 32  # how many small steps to split the arm into
SHRINK = 0.55  # how much sub branches shrink each recursion
STAR_INTERVAL = 4  # place a star every few steps on an arm
MIN_LENGTH_TO_DRAW = 10  # stop it if length becomes smaller than this

screen = turtle.Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.width(2)

# Turn off animation to draw fast then show final image, friends taught me:3)
turtle.tracer(False)


def draw_star(size, color):
    # Draw a big star in the middle
    # Move the turtle a tiny bit so the circle looks centered.
    # Params:
    # size: how big the star is
    # color: the color of the star
    t.penup()
    # lower the star a tiny bit to make the it appear centered
    t.forward(size * 0.05)
    t.left(90)
    t.forward(size * 0.05)
    t.right(90)

    t.pendown()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()

    t.right(90)
    t.forward(size * 0.05)
    t.left(90)
    t.backward(size * 0.05)
    t.pendown()


def draw_galaxy_arm(level, length, step_angle, steps, shrink_factor, color_index):
    # Purpose: draw one spiral arm using many tiny forward and turn steps
    # Every few steps I put a star
    # The recursive branch makes the galaxy look layered and pretty
    #
    # Parameters:
    # level: how many recursive layers are left
    # length: total length of this arm
    # step_angle: degrees to turn each tiny step
    # steps: how many tiny parts the arm is split into
    # shrink_factor: how much the branch's length is scaled down
    # color_index: which color from colors is used
    #
    # Base case:
    #  Stop when level <= 0 or length is smaller than MIN_LENGTH_TO_DRAW.
    #  This keeps my galaxy from recursing forever or drawing uselessly tiny bits
    #
    # How it works:
    #  Save the turtle's start position so we can return later
    #  Walk forward a tiny bit (step_length), turn a little to make a spiral
    #  Every STAR_INTERVAL steps I draw a star (little colored filled circle)
    #  At some of those stars, move out a bit, turn a little so it don't cover the "parent", and call this same function with level-1 to make a child arm.
    #  After a child finishes, go back to the start and keep drawing the parent arm
    # That's all :3
    if level <= 0 or length < MIN_LENGTH_TO_DRAW:
        return
    # Save starting so we can return later
    start_pos = t.position()
    start_heading = t.heading()
    # Choose color for this arm
    arm_color = random.choice(COLORS)
    t.pencolor(arm_color)
    t.pensize(level + 1)
    # I'm drawing the arm as many small steps and call it stepps
    step_length = length / steps
    # draw a tiny straight segment
    for i in range(steps):
        t.pendown()
        t.forward(step_length)
        t.left(step_angle)
        # turn slightly to form a spiral
        if i == steps - 1:
            t.backward(step_length * 0.08)
        # sometimes move slightly backward to kind of overlap

        # Every STAR_INTERVAL steps place a star
        if (i % STAR_INTERVAL) == 0:
            # draw a star with a contrasting color
            saved_pos = t.position()
            saved_heading = t.heading()
            # Draw star
            draw_star(size=max(1.5, level * 1.8), color=arm_color)

            # Decide to spawn a recursive child arm here or not
            should_spawn = (level > 1) and (
                random.random() < 0.5 or (i % (STAR_INTERVAL * 2) == 0)
            )
            # Move slightly outward and rotate to make the child arm branch
            if should_spawn:
                t.penup()
                t.goto(saved_pos)
                t.setheading(saved_heading)
                t.right(14 + (i % 7))
                t.forward(step_length * 1.2)
                t.pendown()
                # Turn a random tiny angle so branches don’t look the same
                # create a smaller arm
                draw_galaxy_arm(
                    level - 1,
                    length * shrink_factor,
                    step_angle * (0.9 + (random.random() * 0.2)),
                    max(6, int(steps * shrink_factor)),
                    shrink_factor,
                    color_index + 1,
                )
                # Return to the star spot and continue parent arm
                t.penup()
                t.goto(saved_pos)
                t.setheading(saved_heading)
                t.pendown()
    # After drawing the whole arm it reset to starting
    t.penup()
    t.goto(start_pos)
    t.setheading(start_heading)
    t.pendown()


def main():
    t.penup()
    t.goto(0, 0)
    t.setheading(0)
    t.pendown()
    # Draw several main spiral arms around the center
    for arm in range(NUM_ARMS):
        t.penup()
        t.goto(0, 0)
        angle_offset = (360 / NUM_ARMS) * arm
        t.setheading(angle_offset)
        t.forward(6)
        t.pendown()
        # vary  the color a bit
        color_index = random.randint(0, len(COLORS) - 1)

        draw_galaxy_arm(
            START_LEVEL, START_LENGTH, STEP_ANGLE, STEPS_PER_ARM, SHRINK, color_index
        )
        # Move back to center to get ready for the next arm
        t.penup()
        t.backward(6)
        t.goto(0, 0)
        t.pendown()
    # Super bright star in the middle of the galaxy
    t.penup()
    t.goto(0, -6)
    t.setheading(0)
    t.pendown()
    draw_star(size=12, color="White")

    t.hideturtle()
    turtle.done()


main()
