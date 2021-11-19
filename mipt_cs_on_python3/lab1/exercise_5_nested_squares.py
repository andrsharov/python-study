import turtle
import time

a = int(input("Введите сторону квадрата a = "))
s = int(input("Введите расстояние между кватратами s = "))
k = int(input("Введите количество квадратов: k = "))

#turtle.shape('turtle')

#hypotenuse = (2*a**2)**(1/2)

for q in range(0, k):
  for i in range(0, 4):
    turtle.forward(a)
    turtle.left(90)
  a += 2*s
  turtle.penup()
  turtle.backward(s)
  turtle.right(90)
  turtle.forward(s)
  turtle.left(90)
  turtle.pendown()

time.sleep(10)
