import turtle

painter = turtle.Turtle()

for _ in range(18):
    # can use _ as a placeholder
    # remember that in range() is upper bound exclusive, so [0,4)
    painter.forward(100)
    painter.left(100)

turtle.done()