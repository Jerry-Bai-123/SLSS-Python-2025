import turtle

t = turtle.Turtle()
t.left(90)  # point upward
t.speed("fastest")


def draw_tree(level: int, branch_length: float):
    """Draw a simple 2-branch recursive tree"""
    if level > 0:
        t.forward(branch_length)
        t.left(47)
        draw_tree(level - 1, branch_length * 0.8)
        t.right(94)
        draw_tree(level - 1, branch_length * 0.8)
        t.left(47)
        t.backward(branch_length)


def draw_complicated_tree(level: int, branch_length: float):
    """Draw a slightly more complicated tree (>2 branches and asymmetric)"""
    if level > 0:
        t.forward(branch_length)
        # Asymmetric: three branches with uneven angles
        t.left(40)
        draw_complicated_tree(level - 1, branch_length * 0.7)
        t.right(60)
        draw_complicated_tree(level - 1, branch_length * 0.6)
        t.right(40)
        draw_complicated_tree(level - 1, branch_length * 0.5)
        # Return to original direction and position
        t.left(60)
        t.backward(branch_length)


# --- Try one at a time ---
# draw_tree(5, 80)
draw_complicated_tree(5, 80)

turtle.done()
