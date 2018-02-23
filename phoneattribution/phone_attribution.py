from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
phone = ""
if len(sys.argv) > 1:
    phone = sys.argv[1]
else:
    phone = input("请输入手机号：")
url = "http://www.ip138.com:8080/search.asp?action=mobile&mobile="+phone
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
tables = bsObj.findAll("table") #查找页面表格
table = tables[1] #获取第二个表格
data = table.findAll("td", {"class": "tdc2"}) #获取表格里有用的td
phone = str(data[0].text)[:-7]
city = str(data[1].text)
type = str(data[2].text)
number = str(data[3].text)
postcode = str(data[4].text)[:6]
text = "手机号码："+phone+"\n"
text = text + "归属地："+city+"\n"
text = text + "卡类型："+type+"\n"
text = text + "区号："+number+"\n"
text = text + "邮编："+postcode
print(text)
