import turtle
import time

k = int(input('Введите количество сторон правильного многоугольника: '))
l = int(input('Введите длинну стороны правильного многоугольника: '))

turtle.shape('turtle')

for i in range(0, k):
  turtle.left(360/k)
  turtle.forward(l)

time.sleep(5)
