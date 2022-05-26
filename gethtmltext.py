from bs4 import BeautifulSoup
import requests
def getUrls(url):   #获取该网页中所有链接
    r=requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding ='utf-8'
    print(r.text)
    href_list = []
    soup = BeautifulSoup(r.text)
    t1=soup.find_all('a')
    for t2 in t1:
        t3=t2.get('href')  #得到超链接
        href_list.append(t3)    #将超链接放入列表中
    return href_list
def getText(url):   #输出网页内容
    try:
        urls = getUrls(url)
        for i in range(len(urls)):  #递归方法遍历所有网页
            if urls[i] not in allurls:  #访问过的超链接不再访问，避免嵌套
                allurls.append(urls[i])
                getHtmlText(urls[i])
    except:
        return " "
def getHtmlText():  #主程序
    url=input("请输入一个网址：")
    global allurls
    allurls=[]  
    getHtmlText(url)
      

