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

def draw_shape(sides, length):
    angle = 360 / sides
    for i in range(sides):
        tina.forward(length)
        tina.left(angle)
            
def trigger(x, y):
    tina.clear()
    sides= int(input("How many sides should the shape have?"))
    length= int(input("How long should each side be?"))
    draw_shape(sides, length)

ws.onscreenclick(trigger)


turtle.done()
