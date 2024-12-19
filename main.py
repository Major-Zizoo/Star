import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(500,500)

pen=turtle.Turtle()
pen.color("aqua")
pen.width(7)

pen.begin_fill()
pen.fillcolor("blue")

pen.forward(100)

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

pen.penup()
pen.right(150)
pen.forward(50)

pen.pendown()
pen.right(90)

pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.end_fill()
turtle.done()