from turtle import *

penup()
goto(-100,-50)
pendown()
forward(200)
left(90)
forward(150)
goto(-100,-50)

def triangle_area(l, h):
    s = l * h /2
    return s

area = triangle_area(200, 150)

penup()
goto(-100,-75)
write("The area of this triangle is: "+str(area), False, "left", ("Arial", 12, "normal"))