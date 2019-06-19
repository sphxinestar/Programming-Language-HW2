import urllib.request
import re
import matplotlib.pyplot as plt

author1 = input("Input Author : ")  #這行可以讓使用者輸入作者名稱
author = author1.replace(" ","+") #把空白鍵利用+號取代
url = "https://arxiv.org/search/?query=" + author + "&searchtype=all"
content = urllib.request.urlopen(url)
html_str = content.read().decode('utf-8')
pattern = "title is-clearfix[\s\S]*?<span"
result = re.findall(pattern, html_str)

for x in result:
    #print(x)
    page = x.split("of")[1].split("result")[0].strip() #print發現不能以字串的方式顯示出來,所以就用分割還有清除頭尾的strip去處理字串

page = int(page)
page = int(page/50 + 1)
#print(page)  #這裡是用來計算我們要跑幾個頁數用的

year = []
#a = 0 #不能在這裡宣告 因為到第二頁的時候就會發現它找不到因為加到51
for x in range(page): #迴圈是從0開始到小於page那個數字 #要記得加range
    url = "https://arxiv.org/search/?query=" + author + "&searchtype=all&start=" + str(x*50)
    content = urllib.request.urlopen(url)
    html_str = content.read().decode('utf-8')
    pattern = "originally announced</span>[\s\S]*?</p>"
    result = re.findall(pattern, html_str)
    searchauthorpattern = "Authors:[\s\S]*?</p>"
    searchauthorresult = re.findall(searchauthorpattern, html_str)
    #print(searchauthorresult)    
    a = 0
    for y in result:
        element = y.split("originally announced</span>")[1].split("</p>")[0].strip()
        element = element.split(" ")[1].split(".")[0]
        #print(element)
        if re.search(author1,searchauthorresult[a]) == None: #因為searchauthorresult是一個陣列,第一筆存第一篇文章內的所有作者,所以用search來找這個作者有沒有在作者欄內
            a = a + 1    
        else:
            year.append(element) #加上append把元素加進去year陣列
            a = a + 1
#print(year)

year.reverse()
#print(year)
dict = {} #用來統計每個元素出現的數量
for key in year:
    dict[key] = dict.get(key,0)+1 #固定用法
#print(dict)

print("[ Author: " + author + " ]")

name = []
values = [] #分別把年份跟每次出現的次數從dict裡面取出來
for x in dict:
    name.append(x)
    values.append(dict[x])
plt.bar(name,values)
plt.title(author)
plt.show()





