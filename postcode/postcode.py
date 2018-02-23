from urllib.request import urlopen
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import sys
content = ""
if len(sys.argv) > 1:
    content = sys.argv[1]
else:
    content = input("请输入地区或者邮编：")
data1 = {
    "area": content.encode("gb2312"), #居然是gb2312 不可原谅
    "action": "area2zip"
}
data2 = {
    "zip": content,
    "action": "zip2area"
}
data = urlencode(data2)
try:
    int(content)
except:
    data = urlencode(data1)
url = "http://www.ip138.com/post/search.asp?"+data #又是ip138 哈哈哈
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
td = bsObj.findAll("td", {"class": "tdc2"}) #这个tdc2感觉已经用了好多遍了
td = td[1]
text = str(td.text)
if "更详细的" in text:
    print("输入数据有误")
else:
    print(text)
