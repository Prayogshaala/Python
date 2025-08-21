## Python day 19 Etch-s-sketch using turtle

import turtle as t


flash=t.Turtle()
screen=t.Screen()

def move_forward():
    flash.forward(10)

def move_backword():
    flash.back(10)

def turn_left():
    flash.left(10)

def turn_right():
    flash.right(10)

def clear_Screen():
    flash.clear()
    flash.up()
    flash.home()
    flash.down()

screen.listen()
screen.onkey(key='w',fun=move_forward)
screen.onkey(key='s',fun=move_backword)
screen.onkey(key='a',fun=turn_left)
screen.onkey(key='d',fun=turn_right)
screen.onkey(key='c',fun=clear_Screen)

screen.exitonclick()

