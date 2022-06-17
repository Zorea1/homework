#七段数码管显示
import datetime,turtle
def drawGap():   #绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):   #绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawDigit(d):  #根据数字绘制七段数码管
    drawLine(True) if d in [2,3,4,5,6,8,9]  else drawLine(False)
    drawLine(True) if d in [0,1,3,4,5,6,7,8,9]  else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,8,9]  else drawLine(False)
    drawLine(True) if d in [0,2,6,8]  else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0,4,5,6,8,9]  else drawLine(False)
    drawLine(True) if d in [0,2,3,5,6,7,8,9]  else drawLine(False)
    drawLine(True) if d in [0,1,2,3,4,7,8,9]  else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)
def drawDate(date):  #获得要输出的数字
    for i in date:
        if i == '年':
            turtle.write('年',font=("Arial",wordsize,"normal"))
    
            turtle.fd(40)
        elif i == '月':
            turtle.write('月',font=("Arial",wordsize,"normal"))
            
            turtle.fd(40)
        elif i == '日':
            turtle.write('日',font=("Arial",wordsize,"normal"))
            
            turtle.fd(40)
        else:
            drawDigit(eval(i))
#显示当前时间       
def displayCurrentDate():
    turtle.Turtle._screen=None
    turtle.TurtleScreen._RUNNING=True
    turtle.penup() 
    turtle.fd(-300)
    drawDate(datetime.datetime.now().strftime('%Y%m%d'))
    turtle.bye()
#显示所输入的时间
def displayDate():
    date=input("请输入年、月、日(如:2016年12月1日):")
    turtle.Turtle._screen=None
    turtle.TurtleScreen._RUNNING=True
    turtle.penup()
    turtle.fd(-350)    
    drawDate(date)
    turtle.bye()
#显示所输入的数字
def displayDigit():
    try:
        num=input("请输入一个整数：")
    except NameError:
        print("输入有误，请输入一个整数！")
    turtle.Turtle._screen=None
    turtle.TurtleScreen._RUNNING=True
    turtle.penup() 
    turtle.fd(-300)
    drawDate(num)
    turtle.bye()
#设置字体大小
def setWordSize():
    try:
        global wordsize
        wordsize=input("请设置字体大小：")
    except NameError:
       print("输入有误，请输入一个整数！")
wordsize = 18 #初始化绘制七段数码管字体大小    
