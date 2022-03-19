import turtle
length = 200
while length <= 300:
    for i in range(0, 40):
        turtle.pencolor('red')
        turtle.forward(length)
        turtle.right(89)
    length += 40
    break
    turtle.pencolor('green')
    turtle.forward(length)
    turtle.right(89)
    length += 40
