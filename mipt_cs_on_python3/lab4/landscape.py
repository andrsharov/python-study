import graphics as gr

window = gr.GraphWin("andrsharov painting", 500, 500)

sky = gr.Rectangle(gr.Point(0, 0), gr.Point(500, 200))
sky.setFill('blue')

cloud1 = gr.Circle(gr.Point(50,50), 10)
cloud2 = gr.Circle(gr.Point(60,50), 10)
cloud3 = gr.Circle(gr.Point(45,60), 10)
cloud4 = gr.Circle(gr.Point(55,60), 10)
cloud5 = gr.Circle(gr.Point(65,60), 10)
cloud1.setFill('white')
cloud2.setFill('white')
cloud3.setFill('white')
cloud4.setFill('white')
cloud5.setFill('white')
cloud1.setWidth(1)
cloud2.setWidth(1)
cloud3.setWidth(1)
cloud4.setWidth(1)
cloud5.setWidth(1)

sky.draw(window)
cloud1.draw(window)
cloud2.draw(window)
cloud3.draw(window)
cloud4.draw(window)
cloud5.draw(window)

window.getMouse()
window.close()