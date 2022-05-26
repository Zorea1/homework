import drawbig
import hash
import DrawSevenSegDate
import complier
import MatchAnalysis
import gethtmltext
import grammarchecker
#显示主界面
def displayMainMenu():    
    ans=input("""
    请选择一个功能：
      1.绘制图形
      2.哈希函数
      3.七段数码管显示
      4.编译器：文本词频统计
      5.模拟并分析比赛
      6.网络爬虫访问并获取所有text
      7.语法检查器
    """)
    if ans =='1':
        print("正在执行<绘制图形>程序......")
        drawbig.draw()
        displayMainMenu()
    elif ans =='2':
        print("正在执行<哈希函数>程序......")
        hash.hash()
        displayMainMenu()
    elif ans =='3':
        print("正在执行<七段数码管显示>程序......")
        displaySubMenu()
    elif ans =='4':
        print("正在执行<编译器：文本词频统计>程序......")
        complier.complier()
        displayMainMenu()
    elif ans =='5':
        print("正在执行<模拟并分析比赛>程序......")
        MatchAnalysis.matchAnalysis()
        displayMainMenu()
    elif ans =='6':
        print("正在执行<网络爬虫访问并获取所有text>程序......")
        gethtmltext.getHtmlText()
        displayMainMenu()  
    elif ans =='7':
        print("正在执行<语法检查器>程序......")
        grammarchecker.grammarChecker()
        displayMainMenu()      
#显示七段数码管菜单界面
def displaySubMenu():
    ans3=input("""
      请选择要实现的功能：
        1.显示当前时间
        2.显示所输入的时间
        3.显示所输入的数字
        4.设置字体格式
        5.返回
        """)
    if ans3 =='1':
        DrawSevenSegDate.displayCurrentDate()
        displaySubMenu()
    elif ans3 =='2':
        DrawSevenSegDate.displayDate()
        displaySubMenu()
    elif ans3 =='3':
        DrawSevenSegDate.displayDigit()
        displaySubMenu()
    elif ans3 =='4':
        DrawSevenSegDate.setWordSize()
        displaySubMenu()
    elif ans3 =='5':
        displayMainMenu()
def menu() :  #主程序
   displayMainMenu()    
