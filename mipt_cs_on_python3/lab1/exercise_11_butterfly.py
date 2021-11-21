import turtle
import time  # Only for test purposes


def draw_butterfly(n: int = 1, r: int = 50, s: int = 15):
    """Function which drawing butterfly by using turtle.circle
    :param n: Quantity of butterfly
    :param r: Start radius of circles
    :param s: Step for radius increment
    """
    turtle.shape("turtle")
    turtle.speed(1)
    r = abs(r)
    for i in range(n):
        turtle.setheading(90)
        turtle.circle(r)
        turtle.setheading(90)
        turtle.circle(-r)
        r += s
    return


draw_butterfly(10, 50, 10)  # Run function

time.sleep(5)  # Only for test purposes
