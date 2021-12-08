import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.findall('channel/item')
f = open('news.json', 'w', encoding='utf-8')
stor=[]
for i in items:
    stor.append({'pubDate': i.find("pubDate").text,'title': i.find("title").text})

f.write(json.dumps(stor, ensure_ascii=False,separators=(',\n ',': ')))
f.close()

print('The work is done!')
