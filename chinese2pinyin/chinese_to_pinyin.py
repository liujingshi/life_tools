import re
import sys
data = open("./chinese_to_pinyin.txt", "r", encoding='utf-8') #打开字符文件
data = data.read()
def getOnePinyin(text):
    reRule = text+"([^,]+),"
    one = re.findall(reRule, data) #正则查找拼音
    if len(one) > 0:
        return one[0]
    else:
        return text
def getPinyin(texts):
    pinyin = ""
    for text in texts:
        pinyin = pinyin + getOnePinyin(text) + " "
    return pinyin
text = ""
if len(sys.argv) > 1:
    text = sys.argv[1]
else:
    text = input("请输入要转换的汉语：")
print(getPinyin(text))
