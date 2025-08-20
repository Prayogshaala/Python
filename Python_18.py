from turtle import Turtle,Screen
import random

flash=Turtle()
flash.shape('turtle')


# Draw a square

def draw_square():
    for i in range(4):
        flash.forward(100)
        flash.right(90)



# Dotted line

def draw_dotted_line():
    for pen in range(10):
        if pen%2==0:
            flash.up()
        else:
            flash.down()

        flash.forward(20)


#Draw shapes

def draw_shapes():
    flash.setpos(-60,60)
    flash.clear()
        
    angle=360


    for sides in range(3,11):
        draw_angle=angle/sides
        r=random.random()
        g=random.random()
        b=random.random()
        flash.pencolor(r,g,b)
        for _ in range(sides):
            flash.forward(100)
            flash.right(draw_angle)
    


#Random Color

def random_color():
    r=random.random()
    g=random.random()
    b=random.random()
    rcolor=(r,g,b)
    return rcolor

# Random Walk


def draw_random_walk():
    direction=['left','right']
    flash.width(8)
    flash.speed(10)
    for _ in range(100):
        flash.pencolor(random_color())
        flash.forward(30)
        dir=random.choice(direction)
        if dir=='left':
            flash.left(90)
        else:
            flash.right(90)

def draw_spirograph():
    flash.speed('fastest')
    flash.width(1)
    flash.setposition(0,0)
    flash.clear()
    for _ in range(60):
        flash.right(6)
        flash.pencolor(random_color())
        flash.circle(100)

draw_square()
flash.clear()

draw_dotted_line()
flash.clear()

draw_shapes()
flash.clear()

draw_random_walk()
flash.clear()

draw_spirograph()

screen=Screen()
screen.exitonclick()
