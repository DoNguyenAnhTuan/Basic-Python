# Chèn thư viện đồ họa turtle
import turtle
# Khởi tạo màn hình đồ họa
screen = turtle.Screen()
# thiết lập độ rộng của màn hình đồ họa
screen.setup(400, 400)
#thiết lập hình ảnh nền cho màn hình đồ họa
screen.bgpic("space.gif")
image = "sieunhan.gif"
# Chèn đối tượng hình ảnh vào màn hình đồ họa
screen.addshape(image)
turtle.shape(image)
move_speed = 10
turn_speed = 10


#  thiết lập các hàm
def forward():
  turtle.forward(move_speed)
def backward():
  turtle.backward(move_speed)
def left():
  turtle.left(turn_speed)
def right():
  turtle.right(turn_speed)
# thiết lập không vẽ khi di chuyển
turtle.penup()
# hàm onkey: sẽ gọi các hàm khi bạn nhấn vào các phím tương ứng
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()
