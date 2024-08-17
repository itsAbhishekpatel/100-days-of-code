# importing the turtle module 
# import turtle library
from turtle import Turtle, Screen
# define an object of turtle class belong to turtle module 
# you notice that for the class name Pascal case is used - first letter is captial
# and use parentheis to intialise the object/ construct the object 
# timmy = turtle.Turtle()

#object of class Turtle named as timmy
timmy = Turtle()
print(timmy)
timmy.shape("turtle")   
timmy.color("coral")
timmy.forward(100)

#object of calss Screen names as my_screen
my_screen = Screen()
my_screen.bgcolor("black")
print(my_screen.canvheight)
my_screen.exitonclick()
