# Draw a dashed line
import turtle as t

tinny = t.Turtle()

for _ in range(15):
    tinny.forward(10)
    tinny.penup()
    tinny.forward(10)
    tinny.pendown()
