import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.findall('channel/item')

tags = []
for item in items[0]:
    tags.append(item.tag)

storage = []
for item in items:
    storage.append({})
    for tag in tags:
        try:
            storage[-1][tag] = item.find(tag).text
        except Exception:
            storage[-1][tag] = 'None'

outFile = open('news_extended.json', 'w', encoding='utf-8')
outFile.write(json.dumps(storage, ensure_ascii=False, separators=(',\n ', ': ')))
outFile.close()

print('done')
