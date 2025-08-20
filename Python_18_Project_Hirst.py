import colorgram
import turtle as t
import random

#colors = colorgram.extract("hirst.jpg", 30)

#colors_list=[]
#for color in colors:
#   color_tup=(color.rgb.r, color.rgb.g, color.rgb.b)
#   colors_list.append(color_tup)


t.colormode(255)
colors_list=[(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203), (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]

print(colors_list)

flash=t.Turtle()
flash.speed(11)

def draw_dot():
    flash.down()
    flash.begin_fill()
    flash.circle(10)
    flash.end_fill()


y=-200

for ver in range(10):
    x=-200
    for hor in range(10):
        flash.up()
        flash.color(random.choice(colors_list))
        flash.setposition(x,y)
        draw_dot()
        x=x+50
    y=y+50
    


screen=t.Screen()
screen.exitonclick()
