from random import random
def printIntro():  #介绍程序功能
    print("这个程序模拟两个选手A和B的某种竞技比赛")
    print("运行程序需要A和B的能力值,失误概率以及天气情况(能力值和失误概率均以0到1之间的小数表示)")
def getInputs():   #输入
    a,b = getProb()
    n=eval(input("模拟比赛的场次："))
    return a, b, n
def getProb():    #获得选手总能力值
    capA=eval(input("请输入选手A的能力值:"))
    capB=eval(input("请输入选手B的能力值:"))
    misplayA=eval(input("请输入选手A的失误概率:"))
    misplayB=eval(input("请输入选手B的失误概率:"))
    weather=input("请输入比赛时的天气情况（例如：晴、多云、雨、雪）：")
    if weather == '晴' :
        weatherA, weatherB=1.0,1.0
    elif weather == '多云' :
        weatherA, weatherB=0.9,0.8
    elif weather == '雨' :
        weatherA, weatherB=0.3,0.7
    elif weather == '雪' :
        weatherA, weatherB=0.2,0.6
    probA = 0.8*capA + 0.15*(1-misplayA) + 0.05*weatherA
    probB = 0.8*capB + 0.15*(1-misplayB) + 0.05*weatherB
    return probA, probB
def simNGames(n, probA, probB):  #模拟n场比赛，得到选手获胜次数
    winsA, winsB=0,0
    for i in range(n):
        scoreA, scoreB=simOneGame(probA, probB)
        if scoreA>scoreB:
            winsA += 1
        else:
            winsB += 1
    return winsA, winsB            
def gameOver(a, b):  #比赛结束的条件
    return a==15 or b==15
def simOneGame(probA,probB):  #模拟一场比赛
    scoreA, scoreB=0,0
    serving = "A"
    while not gameOver(scoreA,scoreB):
        if serving == "A":
            if random() < probA:
                scoreA += 1
            else:
                serving="B"
        else:
            if random() < probB:
                scoreB += 1
            else:
                serving="A"   
    return scoreA, scoreB                     
def printSummary(winsA, winsB):  #输出比赛结果
    n = winsA + winsB
    print("竞技分析开始，共模拟{}场比赛".format(n))
    print("选手A获胜{}场比赛，占比{:0.1%}".format(winsA,winsA/n))
    print("选手B获胜{}场比赛，占比{:0.1%}".format(winsB,winsB/n))
def matchAnalysis():   #主程序
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
