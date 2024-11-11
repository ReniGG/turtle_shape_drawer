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
     
    tina.penup()
    tina.goto(x,y)
    tina.pendown()
    
    try:
        sides= int(input("How many sides should the shape have?"))
        length= int(input("How long should each side be?"))

        if sides <= 0 or length <= 0:
            print("Please enter positive numbers only.")
            sys.exit()  # Exit the program if invalid data is entered

        draw_shape(sides, length)
        turtle_color = (random.random(), random.random(), random.random())
        tina.color(turtle_color)

    except ValueError:
        print("Please enter numbers only.")
        sys.exit()  # Exit the program if non-integer input is provided

ws.onscreenclick(trigger)


turtle.done()
