def inputTxt():  #输入要查找的文件
    path=input("请输入要查找的文件路径(如：桌面/homework/menu.txt):")
    return path
def getText():  #整理文件
    txt = open(inputTxt(),"r").read()
    txt = txt.lower()
    for ch in '!@#$%^&*()_+-=`~[]{\}|:;",.<>/?':
        txt = txt.replace(ch," ")
    return txt
def countTxt():#  统计文件词频
    includes = {"False","None","True","and","as","assert","break","class","continue","def","del","elif","else","except","finally","for","from","global","if","import","in","is","lambda","nonlocal","not","or","pass","raise","return","try","while","with","yield"}
    menuTxt = getText()
    words = menuTxt.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) + 1
    items = list(counts.items())
    items.sort(key = lambda x:x[1], reverse = True)
    for word in includes:
        if word in counts:
            print ("{} {} ".format(word,counts[word]))
def complier():  #主程序
    countTxt()
