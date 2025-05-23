import turtle
def c1():
    t = turtle.Pen()
    t.reset()
    t.up()
    t.goto(-165,0)
    t.down()
    t.width(10)
    t.color("blue")
    t.circle(75)

def c2():
    t = turtle.Pen()
    t.reset()
    t.up()
    t.goto(0,0)
    t.down()
    t.width(10)
    t.color("black")
    t.circle(75)

def c3():
    t = turtle.Pen()
    t.reset()
    t.up()
    t.goto(165,0)
    t.down()
    t.width(10)
    t.color("red")
    t.circle(75)

def c4():
    t = turtle.Pen()
    t.reset()
    t.up()
    t.goto(-82.5,-85)
    t.down()
    t.width(10)
    t.color("yellow")
    t.circle(75)

def c5():
    t = turtle.Pen()
    t.reset()
    t.up()
    t.goto(82.5,-85)
    t.down()
    t.width(10)
    t.color("green")
    t.circle(75)
# gọi hàm
c1()
c2()
c3()
c4()
c5()
