def checkTxt():   #扫描代码文件
    for i in range(len(words)):
        if words[i] == 'for':
            checkFor(i)
        elif words[i] == 'try':
            checkTry(i)
        elif words[i] == 'if':
            checkIf(i)  
        else:
            continue      
#检查for语法
def checkFor(i):
    if words[i+2] == 'in' and words[i+4] == ':' :
        print("for循环语法正确")
    else:
        global countforerror  
        countforerror += 1
        print("for循环语法错误")
#检查try语法
def checkTry(i):
    if words[i+1] == ':' and 'except' in words[i:] :
        for j in range(i+1,len(words)):
            if words[j] == 'except':
                break
        if words[j+1] == ':' or words[j+2] == ':':
            print("try语法正确")
        else :
            global counttryerror 
            counttryerror += 1
            print("try语法错误")   
    else:
        counttryerror += 1 
        print("try语法错误") 
#检查if语法
def checkIf(i):
    if words[i+2] in {'<','>','<=','>=','==','!=','and','or','in','not'}:
        if words[i+2] == 'not':  #检查 not in 情况
            if words[i+3] == 'in' and words[i+5] == ':':
                print("if语法正确")
            else:    
                global countiferror 
                countiferror += 1
                print("if语法错误")
        if words[i+4] == ':' :
            print("if语法正确")
        else:
            countiferror += 1
            print("if语法错误")
    else:
        countiferror += 1
        print("if语法错误")       
def grammarChecker():   #主程序
    #text = open(input("请输入要检查的代码的txt文件地址:"),"r").read()
    text = open("桌面/homework/menu.txt","r").read()
    global words
    words = text.split()   
    wordlist = {"for","try","if"}
    global countforerror,counttryerror,countiferror
    countforerror=0;counttryerror=0;countiferror=0
    checkTxt()
    print("语法检查完毕，共计{}个'for'错误,{}个'try'错误,{}个'if'错误".
        format(countforerror,counttryerror,countiferror))    
    #print (words)  
#grammarChecker()       