import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.findall('channel/item')
newsFile = open('news.json', 'w', encoding='utf-8')
result = []
for i in items:
    result.append({'pubDate': i.find("pubDate").text, 'title': i.find("title").text})

newsFile.write(json.dumps(result, ensure_ascii=False, separators=(',\n ', ': ')))
newsFile.close()