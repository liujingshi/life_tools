import time
import json
import re
import sys
import requests
from urllib.parse import urlencode
from urllib.request import urlopen
from bs4 import BeautifulSoup
header = {  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
session = requests.session()
def getCityUrl(cityName):
    datas = {
        "cityname" : cityName,
        "callback" : "success_jsonpCallback",
        "_" : int(time.time()*1000)
    }
    data = urlencode(datas)
    url = "http://toy1.weather.com.cn/search?"+data #搜索目标城市的url
    html = session.get(url, headers=header) #关键字搜索城市
    jsonp = html.text
    try:
        search = json.dumps(json.loads(jsonp[22:-1])[0]) #取搜到的第一个城市
    except:
        return False
    cityCode = re.findall("{\"ref\": \"([0-9]+)~", search)[0] #匹配城市的编码
    cityUrl = "http://www.weather.com.cn/weather/"+cityCode+".shtml" #目标城市的url
    return cityUrl

def getCityName(cityUrl):
    html = urlopen(cityUrl) #打开天气预报的url
    bsObj = BeautifulSoup(html.read(), "html.parser")
    cityName = bsObj.find("div", {"class": "crumbs fl"}) #找到城市名称
    cityNameStr = str(cityName.text).replace("\n", "").replace(" ","") #替换空格和换行得到完整的城市名称
    return cityNameStr

def getCityWeather(cityUrl):
    html = urlopen(cityUrl)
    bsObj = BeautifulSoup(html.read(), "html.parser")
    ul = bsObj.find("ul", {"class": "t clearfix"})  # 找到天气信息
    h1s = ul.findAll("h1")
    dates = []  # 日期
    for h1 in h1s:
        dates.append(str(h1.text))
    ps = ul.findAll("p", {"class": "wea"})
    weas = []  # 天气
    for p in ps:
        weas.append(str(p.text))
    ems = ul.findAll("em")
    maxs = []  # 风向
    for em in ems:
        spans = em.findAll("span")
        max = ""
        for span in spans:
            max = max + " " + str(span['title'])
        maxs.append(max)
    winps = ul.findAll("p", {"class": "win"})
    mins = []  # 风级
    for winp in winps:
        mins.append(str(winp.i.text))
    temps = ul.findAll("p", {"class": "tem"})
    wds = []  # 温度
    for temp in temps:
        wds.append(str(temp.text).replace("\n", ""))
    weaDatas = []
    i = 0
    for date in dates:
        data = "================\n"
        data = data + date + " -> "
        data = data + weas[i] + " => "
        data = data + wds[i] + " => "
        data = data + maxs[i] + "->"
        data = data + mins[i] + "\n"
        i = i + 1
        weaDatas.append(data)
    return weaDatas

city = "北京"
if len(sys.argv) > 1:
    city = sys.argv[1]
else:
    city = input("请输入城市：")
if not getCityUrl(city):
    print("城市名有误")
    exit()
cityUrl = getCityUrl(city)
cityName = getCityName(cityUrl)
citydatas = getCityWeather(cityUrl)
weather = cityName+"\n"
for citydata in citydatas:
    weather = weather + citydata
print(weather)
