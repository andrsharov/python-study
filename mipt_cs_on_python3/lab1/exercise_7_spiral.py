import turtle
import time
import math

l = int(input("Input spiral lenght l = "))

turtle.shape('turtle')

for i in range(l):
    t = i / 20 * math.pi
    x = (1 + 1 * t) * math.cos(t)
    y = (1 + 1 * t) * math.sin(t)
    turtle.goto(x, y)

time.sleep(5)
