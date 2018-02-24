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
content = "你好"
if len(sys.argv) > 1:
    content = sys.argv[1]
else:
    content = input("请输入要翻译的内容：")
datas = {
    "callback": "sugg1",
    "q": content,
    "dict": "dict",
    "s": "dict",
    "lt": "zh-cn"
}
datas = urlencode(datas)
url = "http://apis.dict.cn/apis/suggestion.php?"+datas
html = session.get(url, headers=header)
rstStr = str(html.text)[6:-2]
jsonObj = json.loads(rstStr)
text = str(jsonObj['s'][0]['e']).replace(";&nbsp;", "\n").replace("; ", "\n").replace(";", "\n")
print(text)
