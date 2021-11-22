import turtle
import time  # Only for test purposes


def draw_circle(r: int = 15, pen_color: str = "black", fill_color: str = None, f: bool = False, x: int = 0, y: int = 0):
    """Function which drawing spring by using turtle.circle
    :param r: Radius of the circle
    :param pen_color: Pen color of the circle. Default is black.
    :param fill_color: Fill color of the circle
    :param f: Enable or disable filling. True or False. Default is False
    :param x: X Coordinate of center of circle
    :param y: Y Coordinate of center of circle
    """
    r = abs(r)  # Ensure than radius is always positive
    turtle.shape("turtle")
    turtle.speed(1)
    turtle.penup()
    turtle.pencolor(pen_color)  # Set pencolor of the circle
    turtle.fillcolor(fill_color)  # Set fill color of the circle
    if f:
        turtle.begin_fill()
    turtle.setposition(x, y - r)
    turtle.pendown()
    turtle.circle(r)
    if f:
        turtle.end_fill()
    turtle.penup()
    return


def draw_arc(r: int = 15, a: int = 180, pen_color: str = "black", pen_heading: int = 90, pen_size: int = 1, x: int = 0, y: int = 0):
    """
    Function which drawing arc by using turtle.circle
    :param r: Arc radius in pixels. Positive number. Default is 15 pixels.
    :param a: Arc angle. Default is 180 degrees (semicircle).
    :param pen_color: Arc color. String. Default is black.
    :param pen_heading: Setup heading. Default is 90 degrees.
    :param pen_size: Arc size. Positive number. Default is 1.
    :param x: X Coordinate of start of arc
    :param y: Y Coordinate of start of arc
    :return: None
    """
    r = abs(r)  # Ensure than radius is always positive
    a = abs(a)  # Ensure than angle is always positive
    pen_size = abs(pen_size)  # Ensure than pen size is always positive
    turtle.shape("turtle")
    turtle.speed(1)
    turtle.penup()
    turtle.setposition(x, y)
    turtle.setheading(pen_heading)
    turtle.pensize(pen_size)
    turtle.pencolor(pen_color)
    turtle.pendown()
    turtle.circle(-r, a)
    turtle.penup()

    return


draw_circle(90, "black", "yellow", True, 90, 90)  # Draw head
draw_circle(15, "black", "blue", True, 60, 135)  # Draw left eye
draw_circle(15, "black", "blue", True, 120, 135)  # Draw right eye
draw_arc(45, 180, "red", 270, 3, 135, 60)  # Draw mouth
# Draw nose
turtle.penup()
turtle.setposition(90, 75)
turtle.setheading(90)
turtle.color("black")
turtle.pensize(3)
turtle.pendown()
turtle.forward(30)
turtle.penup()

time.sleep(5)  # Only for test purposes