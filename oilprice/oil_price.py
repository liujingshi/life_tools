from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
html = urlopen("http://www.bitauto.com/youjia/")
bsObj = BeautifulSoup(html.read(), "html.parser")
table = bsObj.find("table", {"class": "oilTable"}) #获取油价表
tbody = table.tbody
aobjs = tbody.findAll("a") #获取城市名
citys = []
for a in aobjs:
    citys.append(str(a.text))
tds = tbody.findAll("td") #获取油价
prices = []
for td in tds:
    prices.append(str(td.text))
datas = {}
i = 0
for city in citys:
    price = {}
    price['89'] = prices[i]
    i = i + 1
    price['92'] = prices[i]
    i = i + 1
    price['95'] = prices[i]
    i = i + 1
    price['0'] = prices[i]
    i = i + 1
    datas[city] = price;

city = "北京"
if len(sys.argv) > 1:
    city = sys.argv[1]
else:
    city = input("请输入省份：")
if city[-1:] == "省" or city[-1:] == "市":
    city = city[:-1]
if city not in datas:
    print("请输入正确的省份")
    exit()
text = city + "今日油价\n"
text = text + "89号汽油：" + datas[city]['89'] + "\n"
text = text + "92号汽油：" + datas[city]['92'] + "\n"
text = text + "95号汽油：" + datas[city]['95'] + "\n"
text = text + "0号柴油：" + datas[city]['0']
print(text)
