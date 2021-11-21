import turtle
import time  # Only for test purposes


def draw_flower(n: int = 2, r: int = 50):
    """Function which drawing flower by using turtle.circle
    :param n: Quantity of circles
    :param r: Radius of circles
    """
    angle_heading = 360 / n
    angle = 0
    turtle.shape("turtle")
    turtle.speed(1)
    for i in range(n):
        turtle.setheading(angle)
        turtle.circle(r)
        angle += angle_heading
    return


draw_flower(6, 100)  # Run function

time.sleep(15)  # Only for test purposes
