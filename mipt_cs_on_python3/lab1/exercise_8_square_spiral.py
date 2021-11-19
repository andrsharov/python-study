import turtle
import time

l = int(input("Input spiral start length l = "))
k = int(input("Input spiral step k = "))
i = int(input("Input spiral iterations i = "))

turtle.shape('turtle')

for q in range(i):
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    l += k

time.sleep(5)
