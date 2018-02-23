import requests
from urllib.parse import urlencode
import json
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
session = requests.session()
postid = ""
if len(sys.argv) > 1:
    postid = sys.argv[1]
else:
    postid = input("请输入快递单号：")
postdata = {
    "resultv2": 1,
    "text": postid
}
data = urlencode(postdata)
url = "http://www.kuaidi100.com/autonumber/autoComNum?"+data
html = session.post(url, data=postdata, headers=header) #获取快递公司类型
typeJson = json.loads(str(html.text))
if "num" not in typeJson:
    print("请输入正确的快递单号")
    exit()
types = typeJson['auto'] #得到所有可能的快递公司
for type in types: #尝试所有有可能的快递公司
    data = {
        "type": type['comCode'],
        "postid": postid,
        "temp": 0.3069951635340351 #这是参数是什么目前没有研究明白 快递100每次这个参数都会变 但是我发现不变也行
    }
    data = urlencode(data)
    url = "http://www.kuaidi100.com/query?"+data
    html = session.post(url, data=data, headers=header) #查询物流
    htmlJson = json.loads(html.text)
    if htmlJson['message'] == "ok":
        text = "快递单号：" + htmlJson['nu'] + "\n"
        datas = htmlJson['data']
        for data in datas:
            text = text + "================" + "\n"
            text = text + data['time']
            text = text + " -> " + data['context'] + "\n"
        print(text)
        exit()

print("查询失败 请检查单号")

