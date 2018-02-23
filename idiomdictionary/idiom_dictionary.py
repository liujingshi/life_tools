from bs4 import BeautifulSoup
import requests
import sys
header = {  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding":"gzip, deflate",
            "Accept-Language":"zh-CN,zh;q=0.8",
            "Cache-Control":"max-age=0",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
idiom = ""
if len(sys.argv) > 1:
    idiom = sys.argv[1]
else:
    idiom = input("请输入成语：")
session = requests.session()
data = {
    "q": idiom
}
url = "https://chengyu.911cha.com/"
html = session.post(url, data=data, headers=header) #向本身post成语获取成语所在url
if "没有找到相关成语" in str(html.text):
    print("无相关短语")
    exit()
bsObj = BeautifulSoup(html.text, "html.parser")
script = str(bsObj.find("script").text) #提取成语url所在位置
html = session.get(url+script[24:-2], headers=header) #拼接完整url 打开url
bsObj = BeautifulSoup(html.text, "html.parser")
div = bsObj.find("div", {"class": "mcon bt noi f14"})
text = str(div.p.text)[5:] #获取成语解释
print(text)
