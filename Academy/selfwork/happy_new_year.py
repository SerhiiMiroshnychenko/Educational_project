import turtle

turtle.setup(1000, 1000, 0, 0)

mitul = turtle.Turtle()
mitul.width(15)
mitul.color("yellow")
new = turtle.getscreen()
mitul.speed(20)

new.bgcolor("deepskyblue")

# Hidden Work(penup)
mitul.left(180)
mitul.penup()
mitul.forward(300)
mitul.right(90)
mitul.forward(100)
mitul.pendown()

# Printing H
# start to draw
mitul.forward(50)
mitul.right(90)
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.left(90)

mitul.penup()
mitul.forward(50)
mitul.left(90)
mitul.pendown()
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.right(90)
mitul.forward(50)

# printing A
mitul.penup()
mitul.left(90)
mitul.forward(15)
mitul.pendown()
mitul.left(70)
mitul.forward(110)
mitul.right(70)
mitul.right(70)
mitul.forward(110)
mitul.left(180)
mitul.forward(55)
mitul.left(70)
mitul.forward(38)
mitul.left(70)
mitul.penup()
mitul.forward(55)
mitul.left(110)
mitul.forward(100)

# printing P
mitul.left(90)
mitul.pendown()
mitul.forward(100)
mitul.right(90)
mitul.forward(50)
mitul.right(20)
mitul.forward(20)
mitul.right(70)
mitul.forward(40)
mitul.right(70)
mitul.forward(20)
mitul.right(20)
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.left(90)
mitul.penup()
mitul.forward(100)

# printing P
mitul.left(90)
mitul.pendown()
mitul.forward(100)
mitul.right(90)
mitul.forward(50)
mitul.right(20)
mitul.forward(20)
mitul.right(70)
mitul.forward(40)
mitul.right(70)
mitul.forward(20)
mitul.right(20)
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.left(90)
mitul.penup()
mitul.forward(100)

# printing Y
mitul.forward(20)
mitul.pendown()
mitul.left(90)
mitul.forward(50)
mitul.left(30)
mitul.forward(60)
mitul.backward(60)
mitul.right(60)
mitul.forward(60)
mitul.backward(60)
mitul.left(30)

# go Home
mitul.penup()
mitul.home()

mitul.color("dodgerblue")
new.bgcolor("gold")
# setting second row

mitul.backward(300)
mitul.right(90)
mitul.forward(60)
mitul.left(180)

# printing B
mitul.pendown()
mitul.forward(100)
mitul.right(160)
mitul.forward(100)
mitul.left(160)
mitul.forward(100)

# go Home
mitul.penup()
mitul.home()

# setting up
mitul.backward(240)
mitul.right(90)
mitul.forward(10)
mitul.pendown()
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.backward(50)
mitul.left(90)
mitul.forward(100)
mitul.right(90)
mitul.forward(50)
mitul.backward(50)
mitul.right(90)
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.penup()
mitul.home()

# set up for W
mitul.backward(150)
mitul.right(90)
mitul.forward(60)
mitul.pendown()
mitul.backward(100)
mitul.forward(100)
mitul.left(120)
mitul.forward(40)
mitul.right(60)
mitul.forward(40)
mitul.left(120)
mitul.forward(100)
mitul.penup()
mitul.home()

# set up for Y
mitul.backward(30)
mitul.right(90)
mitul.forward(65)
mitul.left(90)

# set up for Y
mitul.pendown()
mitul.left(90)
mitul.forward(50)
mitul.left(30)
mitul.forward(60)
mitul.backward(60)
mitul.right(60)
mitul.forward(60)
mitul.backward(60)
mitul.left(30)

# go Home
mitul.penup()
mitul.home()

# printing E
mitul.forward(10)
mitul.right(90)
mitul.forward(10)
mitul.pendown()
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.backward(50)
mitul.left(90)
mitul.forward(100)
mitul.right(90)
mitul.forward(50)
mitul.backward(50)
mitul.right(90)
mitul.forward(50)
mitul.left(90)
mitul.forward(50)
mitul.penup()
mitul.home()

# set up for A
mitul.forward(90)

# printing A
mitul.right(90)
mitul.forward(50)
mitul.left(90)
mitul.pendown()
mitul.left(70)
mitul.forward(110)
mitul.right(70)
mitul.right(70)
mitul.forward(110)
mitul.left(180)
mitul.forward(55)
mitul.left(70)
mitul.forward(38)
mitul.left(70)
mitul.penup()
mitul.forward(55)
mitul.left(110)
mitul.forward(100)

# go home
mitul.penup()
mitul.home()

# set up for R
mitul.forward(180)
mitul.right(90)
mitul.forward(50)
mitul.left(180)

# set up for R
mitul.pendown()
mitul.forward(100)
mitul.right(90)
mitul.forward(50)
mitul.right(20)
mitul.forward(20)
mitul.right(70)
mitul.forward(40)
mitul.right(70)
mitul.forward(20)
mitul.right(20)
mitul.forward(50)
mitul.left(180)
mitul.forward(50)
mitul.right(20)
mitul.forward(20)
mitul.right(70)
mitul.forward(40)
mitul.left(180)
mitul.penup()
mitul.home()

new.bgcolor("skyblue")

# go to home()
mitul.penup()
mitul.home()

# design pattern
mitul.home()
mitul.forward(370)
mitul.pendown()
mitul.color("yellow")
mitul.width(3)
mitul.speed(0)

def squre(length, angle, color, width):
    mitul.width(width)
    mitul.color(color)
    mitul.forward(length)
    mitul.right(angle)
    mitul.forward(length)
    mitul.right(angle)
    mitul.color(color)
    mitul.forward(length)
    mitul.right(angle)
    mitul.forward(length)
    mitul.right(angle)

length = 80
color = 'yellow'
width = 10
for i in range(79):
    length = 80 - i
    if i % 5 == 0:
        color = 'darkturquoise'
    elif i % 3 == 0:
        color = 'cyan'
    elif i % 2 == 0:
        color = 'gold'
    else:
        color = 'yellow'
    mitul.right(10)
    squre(length, 90, color, width)

mitul.penup()
mitul.home()
mitul.left(90)
mitul.forward(270)
mitul.left(90)
mitul.forward(200)
mitul.pendown()
def draw_star(size, color, bcolor, width):
    mitul.color(color)
    mitul.width(width)
    angle = 120
    mitul.fillcolor(bcolor)
    mitul.begin_fill()

    for _ in range(5):
        mitul.forward(size)
        mitul.right(angle)
        mitul.forward(size)
        mitul.right(72 - angle)
    mitul.end_fill()
    return

draw_star(50,'gold', "deepskyblue", 25)
draw_star(20,'aqua', "yellow", 10)

mitul.penup()
mitul.home()

turtle.mainloop()
