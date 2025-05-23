import turtle
import math
import random
# thiết lập màn hình đồ họa
sc = turtle.Screen()
#thiết lập hình ảnh nền cho màn hình đồ họa
sc.bgpic("space.gif")

# Vẽ vùng giới hạn di chuyển:
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.speed(0)
for i in range(4):
    mypen.forward(600)
    mypen.left(90)
# vẽ xong, ẩn đối tượng vẽ
mypen.hideturtle()

# Tạo ra nhân vật siêu anh hùng
player = turtle.Turtle()
player.color("yellow")
player.shape("turtle")
player.penup()
# thiết lập tốc độ siêu anh hùng
speed = 1

# Tao ra quai vat
goal = turtle.Turtle()
image="quaivat1.gif"
sc.addshape(image)
goal.shape(image)
goal.penup()
goal.speed(0)
goal.setposition(random.randint(-300, 300), random.randint(-300, 300))


# định nghĩa các phím ra chuyển
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def increaseSpeed():
    global speed
    speed += 1
    if speed >= 5:
        speed = 5
def decreaseSpeed():
    global speed
    speed -= 1
    if speed <= -5:
        speed = -5


def isCollision(t1, t2):
    #khoang cach tu nguoi choi den muc tieu:
    d = math.sqrt(math.pow(t1.xcor() - t2.xcor(),2) + math.pow(t1.ycor() - t2.ycor(),2))
    if d<20:
        return True
    else:
        return False
    
def boundaryChecking(t):
    if t.xcor() < -300 or t.xcor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))
    if t.ycor() < -300 or t.ycor() > 300:
        t.right(180)
        t.setposition(random.randint(-300, 300), random.randint(-300, 300))



# khi nhấn phím
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increaseSpeed, "Up")
turtle.onkey(decreaseSpeed, "Down")


# Xử lý khi siêu anh hùng di chuyển va chạm vào biên
while True:
    player.forward(speed)
    #Boundary checking:
    boundaryChecking(player)
    
    #Collission checking (kiem tra va cham)
    if isCollision(player, goal):
        print("Ðã giai cuu the gioi")
        break
        #goal.hideturtle()
        #goal.setposition(random.randint(-300, 300), random.randint(-300, 300))
        #goal.right(random.randint(0,360))

    #Move the goal:
    goal.forward(10)
    goal.left(random.randint(10,180))
    #Boundary checking:
    boundaryChecking(goal)
