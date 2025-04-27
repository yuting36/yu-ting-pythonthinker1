

import turtle 

window = turtle.Screen()

window.setup(width=600 , height=400)
t = turtle.Turtle()
t.shape("turtle")
t.fillcolor("green")


t.pendown
#line:
#t.seth(90)
#t.forward(100)

#square:
t.seth(90)
for i in range (4):
    t.forward(100)
    t.left(90)

# #triangle:
# t.seth(90)
# for i in range (3):
#     t.forward(100)
#     t.left(120)

# #pentagon :
# t.seth(90)
# for i in range (5):   
#     t.forward(100)
#     t.left(72)

# #hexagon :
# t.seth(90)
# for i in range (6):
#     t.forward(100)
#     t.left(60)

#circle :
t.seth(90)
for i in range (360): 
    t.forward(100)
    t.left(1)

t.penup


window.mainloop()