print("Hello from lesson 16")
 
import turtle
t = turtle.Turtle()

# window = t.screen
# window.setup(width=600 , height=400)

# def shape(length,sides):
#     t.pendown
#     t.seth(90)
#     for i in range (sides):
#          t.forward(length)
#          t.left(360 / sides)

# num = 0.1
# while num != 10:
#     shape(num,100)
#     num += 0.1

# window.mainloop()



def screen(Length, Breadth):
    screen = t.screen
    screen.setup(Length , Breadth)
    return screen

def move_ball(ball, dx, dy):
    ball.setx(ball.xcor() + dx)

def ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("black")
    ball.penup()



Slength = 300
Sbreadth = 500
screen = screen(Slength , Sbreadth)
ball = ball()

screen.mainloop()