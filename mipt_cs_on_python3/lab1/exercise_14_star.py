import turtle
import time  # Only for test purposes


def draw_star(n: int = 5, s: int = 150, pen_color: str = "black", fill_color: str = "yellow"):
    """
    Function which drawing star with n sides
    :param n: Number of sides. Must equals or more than 5
    :param s: Star side
    :param pen_color: Border color of the star
    :param fill_color: Fill color of the star
    :return: None
    """
    turtle.speed(1)  # Setup speed
    turtle.color(pen_color)  # Setup color
    turtle.fillcolor(fill_color)  # Setup fill color
    angle = 180.0 - 180.0 / n  # Calculate angle
    turtle.begin_fill()
    for i in range(n):
        turtle.forward(s)
        turtle.left(angle)
    turtle.forward(s)
    turtle.end_fill()
    return


# draw_star(5, 250, "blue", "green")  # Draw 5 sides star
draw_star(11, 250, "black", "yellow")  # Draw 11 sides star

time.sleep(15)  # Only for test purposes
