import turtle
import maths
import math
file = open("./Source/tesla.data","r+")
x=file.readline()
y=file.readline()
mod = int(x[x.find(" ")+2:len(x)])
mult = int(x[x.find(" ")+2:len(x)])
file.close()
turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.forward(348)
turtle.left(90)
turtle.forward(150)
turtle.right(180)
turtle.pendown()
for i in range(mod):
    turtle.pensize(3)
    turtle.forward(1)
    turtle.write(i)
    turtle.write(i)
    turtle.pensize(1)
    for x in range(0,(360/mod)):
        turtle.forward(6)
        turtle.right(1)
print(maths.maths()[0])
input()