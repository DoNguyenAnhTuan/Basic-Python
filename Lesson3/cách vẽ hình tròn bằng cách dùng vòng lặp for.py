from turtle import *
import time
a=Turtle()
cl=['red', 'green','yellow']
x=75
for i in range (3):
                a.penup()
                a.goto(0,-x)
                a.pendown()
                a.circle(x)
                x=x-25
                
