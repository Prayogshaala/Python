from turtle import Turtle, Screen
from prettytable import PrettyTable
my_screen=Screen()

speedy=Turtle()
speedy.color('olive')
speedy.shape('turtle')
speedy.forward(200)
my_screen.exitonclick()


table=PrettyTable()
table.add_column("Pokemon Name",['Pikachu','Suirtle','Charmander'])
table.add_column("Type",['Electric','Water','Fire'])
table.align='l'
print(table)
