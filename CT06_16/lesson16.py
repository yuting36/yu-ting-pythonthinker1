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
    ball.sety(ball.ycor() + dy)
    

def createball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("black")
    ball.penup()
    return ball

def check_x(ball ,Slength):
    if ball.xcor() > (Sbreadth / 2) or ball.xcor() < (-Sbreadth / 2):
            return True

def check_y(ball ,Slength):
    if ball.ycor() > (Slength / 2) or ball.ycor() < (-Slength / 2):
            return True


Slength  = 600
Sbreadth = 600
screen = screen(Slength , Sbreadth)
ball = createball()

dx = 2
dy = 2

while True:
    move_ball(ball, dx ,dy )
    if check_x(ball, Slength):
         dx *= -1
    if check_y(ball, Slength):
         dy *= -1

screen.mainloop()