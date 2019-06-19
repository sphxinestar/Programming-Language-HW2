import urllib.request
import re

author1 = input("Input Author : ")  #這行可以讓使用者輸入作者名稱
author = author1.replace(" ","+") #把空白鍵利用+號取代
url = "https://arxiv.org/search/?query=" + author + "&searchtype=all"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = "title is-clearfix[\s\S]*?<span"
result = re.findall(pattern, html_str)

authornumber = []
for x in result:
    #print(x)
    page = x.split("of")[1].split("result")[0].strip() #print發現不能以字串的方>式顯示出來,所以就用分割還有清除頭尾的strip去處理字串

page = int(page)
page = int(page/50 + 1)
#print(page)  #這裡是用來計算我們要跑幾個頁數用的

for x in range(page): #迴圈是從0開始到小於page那個數字 #要記得加range
    url = "https://arxiv.org/search/?query=" + author + "&searchtype=all&start=" + str(x*50)
    content = urllib.request.urlopen(url)
    html_str = content.read().decode('utf-8')
    pattern = "Authors[\s\S]*?</p>" #改成要尋找作者
    result = re.findall(pattern, html_str)
    a = 0
    for y in result:
        if re.search(author1,result[a]) == None:
            a = a + 1
        else:
            authorpattern = '<a href=\"\/search\/\?searchtype\=author[\s\S]*?</a>'
            authorresult = re.findall(authorpattern, result[a])
            for z in authorresult:
                element = z.split("\">")[1].split("</a>")[0].strip()
                #print(element)
                authornumber.append(element)
            a = a + 1

authornumber.sort()
dict = {}
for key in authornumber:
    dict[key] = dict.get(key,0)+1 #固定用法
dict.pop('Ian Goodfellow')

print("[ Author: " + author + " ]")

name = []
values = []
for x in dict:
    name.append(x) 
    values.append(dict[x])
for y in range(len(name)):
    print("Name of co-author " + name[y] + " : " + str(values[y]) + " times")

#print(name)
#print(values)








