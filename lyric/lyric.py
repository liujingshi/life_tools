import requests
import time
import re
import json
from bs4 import BeautifulSoup
import sys
from urllib.parse import urlencode
session = requests.session()
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
          "Accept-Encoding": "gzip, deflate",
          "Accept-Language": "zh-CN,zh;q=0.8",
          "Cache-Control": "max-age=0",
          "Connection": "keep-alive",
          "Content-Type": "application/x-www-form-urlencoded",
          "Upgrade-Insecure-Requests": "1",
          "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
}
musicName = ""
if len(sys.argv) > 1:
    musicName = sys.argv[1]
else:
    musicName = input("请输入歌名：")
data = {
    "SONGNAME":musicName,
    "ft":"music",
    "rformat":"json",
    "encoding":"utf8",
    "rn":8,
    "callback":"song",
    "vipver":"MUSIC_8.0.3.1",
    "_":int(time.time()*1000)
}
data = urlencode(data)
url = "http://search.kuwo.cn/r.s?"+data
html = session.get(url, headers=headers)
string = str(html.text)
firstFiled = re.findall("\[{(.*)},", string)[0]
fileds = firstFiled.split(',')
name = ""
musicId = ""
for filed in fileds:
    if "'NAME'" in filed:
        if name == "":
            name = filed[8:-1]
    if "'MUSICRID'" in filed:
        if musicId == "":
            musicId = filed[18:-1]
            break
musicUrl = "http://www.kuwo.cn/yinyue/"+musicId
html = session.get(musicUrl, headers=headers)
bsObj = BeautifulSoup(html.text, "html.parser")
script = str(bsObj.findAll("script")[6].text).replace("	","").replace(" ", "").replace("\n", "")
lrcStr = script[12:-5]
lrcs = json.loads(lrcStr)
for lrc in lrcs:
    print(lrc)
