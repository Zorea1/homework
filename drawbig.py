import turtle
def drawBig(color,size,to_angle1,distance1,
        to_angle2,distance2,radius,angle):
    turtle.penup()
    turtle.pensize(size)
    turtle.pencolor(color)
    turtle.seth(to_angle1)
    turtle.fd(distance1)
    turtle.pendown()
    turtle.seth(to_angle2)
    turtle.circle(radius,angle)
    turtle.fd(distance2)
def draw():   #主程序
    turtle.Turtle._screen=None
    turtle.TurtleScreen._RUNNING=True
    drawBig("green",5,180,40,0,80,0,0,)
    drawBig("red",5,135,56.6,-90,40,0,0)
    drawBig("blue",5,-90,0,-90,0,-40,90)
    drawBig("yellow",5,45,56.6,-90,0,40,90)
    turtle.bye()