import turtle
import time

n = int(input("Input quantity legs n = "))
r = int(input("Input len leg r = "))

turtle.shape('turtle')

for q in range(0, n):
  turtle.forward(r)
  turtle.stamp()
  turtle.backward(r)
  turtle.right(360/n)

time.sleep(5)
