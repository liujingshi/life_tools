from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup
import sys
idcard = ""
if len(sys.argv) > 1:
    idcard = sys.argv[1]
else:
    idcard = input("请输入身份证号：")
data = {
    "action": "idcard",
    "userid": idcard,
    "B1": "%B2%E9+%D1%AF"
}
data = urlencode(data)
url = "http://qq.ip138.com/idsearch/index.asp?"+data #ip138是个好东西 哈哈哈哈
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
tds = bsObj.findAll("td", {"class": "tdc2"})
if len(tds) > 0:
    text = "身份证号："+idcard+"\n"
    text = text + "性别："+str(tds[0].text)+"\n"
    text = text + "出生日期："+str(tds[1].text)+"\n"
    text = text + "发证地："+str(tds[2].text)
else:
    text = "身份证号有误"
print(text)
