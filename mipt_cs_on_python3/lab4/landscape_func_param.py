import graphics as gr

window = gr.GraphWin("andrsharov painting", 500, 500)

def draw_cloud(x, y, r):
    cloud = gr.Circle(gr.Point(x, y), r)
    cloud.setFill('white')
    cloud.setWidth(1)
    cloud.draw(window)

def draw_sky(color):
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(500, 200))
    sky.setFill(color)
    sky.draw(window)

def draw_clouds():
    draw_cloud(50, 50, 10)
    draw_cloud(60, 50, 10)
    draw_cloud(45, 60, 10)
    draw_cloud(55, 60, 10)
    draw_cloud(65, 60, 10)

def draw_landscape():
    draw_sky('blue')
    draw_clouds()

draw_landscape()
window.getMouse()
window.close()
