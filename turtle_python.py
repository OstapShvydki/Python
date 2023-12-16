"""
Square
import turtle
my_turtle=turtle.Turtle()
my_turtle.fillcolor("green")
my_turtle.pencolor("blue")
my_turtle.begin_fill()
#my_turtle.forward(100)
# my_turtle.backward(100)
for i in range(4):
    my_turtle.forward(100)
    my_turtle.right(90)
my_turtle.end_fill()
turtle.done()
"""
"""
circle
import turtle
my_turtle=turtle.Turtle()
my_turtle.fillcolor("green")
my_turtle.pencolor ("blue")
my_turtle.begin_fill()
for i in range(360):
    my_turtle.backward(1)
    my_turtle.left(1)
my_turtle.end_fill()
turtle.done
"""
"""
#triangle
import turtle
my_turtle=turtle.Turtle()
my_turtle.fillcolor("green")
my_turtle.pencolor("blue")
my_turtle.begin_fill()
for i in range(3):
    my_turtle.backward(100)
    my_turtle.left(120)
my_turtle.end_fill()
turtle.done()
"""
#rectangle
import turtle
my_turtle=turtle.Turtle()
my_turtle.fillcolor("green")
my_turtle.pencolor("blue")
my_turtle.begin_fill()
for i in range(2):
    my_turtle.backward(100)
    my_turtle.left(90)
    my_turtle.backward(50)
    my_turtle.left(90)
my_turtle.end_fill()
turtle.done()