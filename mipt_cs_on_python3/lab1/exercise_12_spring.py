import turtle
import time  # Only for test purposes


def draw_spring(n: int = 1, R: int = 20, r: int = 5):
    """Function which drawing spring by using turtle.circle
    :param n: Number of coil springs
    :param R: Radius of big coil of spring
    :param r: Radius of small coil of spring
    """
    turtle.shape("turtle")
    turtle.speed(1)
    n = abs(n)
    R = abs(R)
    r = abs(r)
    for i in range(n):
        turtle.setheading(90)
        turtle.circle(-R, 180)  # Draw big coil
        turtle.circle(-r, 180)  # Draw small coil
    turtle.circle(-R, 180)  # Draw the end big coil
    return


draw_spring(4, 50, 10)  # Run function

time.sleep(15)  # Only for test purposes
