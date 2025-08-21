import turtle as t
from random import randint



flash=t.Turtle()
superman=t.Turtle()
greenlantern=t.Turtle()
hulk=t.Turtle()
silversurfer=t.Turtle()

def turtle_appearance(racing_turtle, color):
    racing_turtle.shape('turtle')
    racing_turtle.color(color)

def Set_start_position(racing_turtle, x, y):
    racing_turtle.up()
    racing_turtle.setpos(x,y)

def move_forward(racing_turtle, steps):
    racing_turtle.forward(steps)

def check_turtle_position(racing_turtle):
    return racing_turtle.pos()

turtles=[
    {
        'name':flash,
        'color':'red'
        },
    {
        'name':superman,
        'color':'blue'
        },
    {
        'name':greenlantern,
        'color':'green'
        },
     {
        'name':hulk,
        'color':'yellow'
        },
     {
        'name':silversurfer,
        'color':'silver'
        }
    ]

x=-350
y=-100

for tur in turtles:
    turtle_appearance(tur['name'], tur['color'])
    Set_start_position(tur['name'], x,y)
    y+=50

users_turtle=input("Which turtle you want to place the bet on?").lower()

race_over=0

while race_over==0:
    for tur in turtles:
        move_forward(tur['name'],randint(0,10))
        pos=check_turtle_position(tur['name'])
        if pos[0] >= 350:
            if tur['color']==users_turtle:
                print(f"Congratulation, {tur['color']} has won the race!")
            else:
                print(f"Sorry {tur['color']} has won the race!")
            race_over=1
            break



screen=t.Screen()
screen.exitonclick()
