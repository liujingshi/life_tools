from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import sys
stars = {
    "白羊座": "Aries/",
    "金牛座": "Taurus/",
    "双子座": "Gemini/",
    "巨蟹座": "Cancer/",
    "狮子座": "Leo/",
    "处女座": "Virgo/",
    "天秤座": "Libra/",
    "天蝎座": "Scorpio/",
    "射手座": "Sagittarius/",
    "摩羯座": "Capricorn/",
    "水瓶座": "Aquarius/",
    "双鱼座": "Pisces/"
}
mystar = "白羊"
if len(sys.argv) > 1:
    mystar = sys.argv[1]
else:
    mystar = input("请输入您的星座：")
if mystar == "":
    mystar = "白羊"
if mystar[-1:] != "座":
    mystar = mystar + "座"
if mystar not in stars:
    print("请输入正确的星座")
    exit()
url = "http://www.d1xz.net/yunshi/today/"+stars[mystar]
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
string = str(bsObj)
labels = re.findall("labels: \[\"(爱情[0-9]{2}%\", \"财运[0-9]{2}%\", \"健康[0-9]{2}%\", \"工作[0-9]{2}%\", \"综合[0-9]{2}%)\"\],", string)
luck = str(labels[0]).replace("\", \"", "\n")
divs = bsObj.findAll("div", {"class", "words_t"})
color = str(divs[0].text)
number = str(divs[1].text)
star = str(divs[2].text)
div = bsObj.find("div", {"class": "txt"})
txt = str(div.text)
text = mystar+"今日运势\n"
text = text + luck + "\n"
text = text + "幸运颜色："+color + "\n"
text = text + "幸运数字："+number + "\n"
text = text + "速配星座："+star + "\n"
text = text + txt
print(text)
