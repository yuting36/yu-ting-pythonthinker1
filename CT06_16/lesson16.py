print("Hello from lesson 16")
 
import turtle
t = turtle.Turtle()

window = t.Screen
window.setup(width=600 , height=400)

def shape(length,sides):
    t.pendown
    t.seth(90)
    for i in range (4):
         t.forward(100)
         t.left(90)
