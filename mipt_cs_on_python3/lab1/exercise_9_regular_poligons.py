import turtle
import time  # Only for test purposes
import math


def draw_regular_polygon(n: int = 3, a: int = 50, x: int = 0, y: int = 0):
    """
    Function, which draw the polygon with n sides, with a size, start drawing with x and y coordinates
    :param n: Number of sides of a polygon
    :param a: Side of a regular polygon (in pixels)
    :param x: Start x coordinate
    :param y: Start y coordinate
    :return: None
    """
    # Calculate beta - angle between polygon sides
    beta = 360 / n
    # Calculate start_angle - angle need to first LEFT (!) rotate turtle
    start_angle = 180 - ((n - 2) / n) * 180 / 2
    turtle.penup()
    turtle.speed(1)  # Setup turtle speed
    turtle.setposition(x, y)  # Setup turtle start coordinates
    turtle.shape("turtle")  # Setup turtle shape
    turtle.setheading(0)  # Setup turtle default heading
    turtle.left(start_angle)  # Turn turtle to the start heading position
    turtle.pendown()
    for i in range(0, n):
        turtle.forward(a)
        turtle.left(beta)
    turtle.penup()
    return


def draw_multiple_nested_polygons(start_corner: int = 3, n: int = 3, start_radius: int = 50, step_radius: int = 5):
    """
   Function which draw multiple polygons
    :param step_radius:
   :param start_corner: Quantity corners for the first polygon, must be >= 3
   :param n: Quantity of polygons
   :param start_radius: Radius for the first polygon
   :param step_side: Step for radius increment
   :return: None
   """
    radius = start_radius
    i: int
    for i in range(start_corner, (start_corner + n)):
        side = 2 * radius * math.sin(math.pi / i)
        # print('i=', i, 'side=', side, 'y=', y)  # Only for test purposes
        draw_regular_polygon(i, side, radius, 0)
        radius += step_radius
    return


draw_multiple_nested_polygons(3, 10, 50, 25)

time.sleep(15)  # Only for test purposes