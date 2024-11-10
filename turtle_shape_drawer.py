import turtle
import random

ws = turtle.Screen()
ws.bgcolor("#ff9999")
ws.title("Turtle Shape Drawer 🐢")

tina = turtle.Turtle()
tina.shape("turtle")
tina.color("#99ffe6")
tina.pensize(5)
tina.speed(0)


sides= int(input("How many side should the shape have?"))
length= int(input("How long should be one side?"))

def draw_shape(sides, length):
    angle = 360 / sides
    for i in range(sides):
        tina.forward(length)
        tina.left(angle)
            
draw_shape(sides, length)


tina.color("#ffff99")

turtle.done()
