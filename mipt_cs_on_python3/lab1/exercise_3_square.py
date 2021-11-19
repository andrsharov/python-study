import turtle
import time

a = int(input("Enter the side of the square a = "))

turtle.shape('turtle')

i = 0
while i < 4:
  turtle.forward(a)
  turtle.left(90)
  i += 1

time.sleep(5)
