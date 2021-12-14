import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.findall('channel/item')
outFile = open('news.json', 'w', encoding='utf-8')
storage = []

for item in items:
    storage.append({'pubDate': item.find("pubDate").text, 'title': item.find("title").text})

outFile.write(json.dumps(storage, ensure_ascii=False, separators=(',\n ', ': ')))
outFile.close()

print('done')
