import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.findall('channel/item')

tags = []
for i1 in items[0]:
    tags.append(i1.tag)

stor=[]
for i in items:
    stor.append({})
    for tag in tags:
        try:
            stor[-1][tag] = i.find(tag).text
        except BaseException:
            stor[-1][tag]='None'

f = open('FullNews.json', 'w', encoding='utf-8')
f.write(json.dumps(stor, ensure_ascii=False,separators=(',\n ',': ')))
f.close()

print('ping')