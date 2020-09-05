"""
sin alpha = a / c
cos beta = b / c
"""
import turtle  # import turtle module, allowing us to use turtle commands
import math
turtle.pensize(10)
turtle.pencolor("green")
#triangle
turtle.penup()
turtle.goto(-300, -420)
turtle.pendown()
turtle.forward (500)
turtle.left(90)
turtle.forward(500)
turtle.pencolor("red")
turtle.left(135)
turtle.forward(710)
#Lets find z
turtle.penup()
turtle.goto(-190, 420)
turtle.pendown()
turtle.pencolor("black")
turtle.write("Let's find value of Z", font=("Arial", 36, "bold"))
turtle.penup()
turtle.goto(-100, -160)
turtle.pendown()
turtle.pencolor("black")
turtle.write("z?", font=("Arial", 36, "bold"))
turtle.penup()
turtle.goto(-50, -490)
turtle.pendown()
turtle.pencolor("black")
turtle.write("X", font=("Arial", 36, "bold"))
turtle.penup()
turtle.goto(-220, -400)
turtle.pendown()
turtle.pencolor("black")
turtle.write("", font=("Arial", 36, "bold"))
screen = turtle.Screen()
x = float(screen.textinput("Input", "Input X in meters?"))
b = float(screen.textinput("Input", "Input  in degrees"))
z = float(round((x / math.cos(math.radians(b))), 2))
turtle.penup()
turtle.goto(-30, 220)
turtle.pendown()
turtle.pencolor("black")
turtle.write("Z =           m",  font=("Arial", 36, "bold"))# Here i can't put Z value
turtle.penup()
turtle.goto(70, 220)
turtle.pendown()
turtle.pencolor("black")
turtle.write(z,font=("Arial", 36, "bold") )
turtle.done()  # drawing is finished, do not close window