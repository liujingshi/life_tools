from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "http://www.todayonhistory.com/"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html.parser")
divs = bsObj.findAll("div", {"class": "t"})
dates = []
contents = []
for div in divs:
    dates.append(str(div.span.text))
    contents.append(str(div.a.text))
text = "历史上的今天\n"
i = 0
for date in dates:
    text = text + "===========\n"
    text = text + date + " => " + contents[i] + "\n"
    i = i + 1
print(text)
