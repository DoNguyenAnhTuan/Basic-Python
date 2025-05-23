# giai bai 8: ve tam giac can
from turtle import *

wn = Screen()
norvig = Turtle()

for i in range(3):
    norvig.forward(100)

    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides
    norvig.left(360/3)

#ve hinh chu nhat
kurzweil = Turtle()
for i in range(4):
   kurzweil.forward(100)
   kurzweil.left(360/4)
#ve hinh tron
pen = Turtle()
pen.shape("turtle")
pen.circle(10)
