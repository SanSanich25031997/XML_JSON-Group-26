import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.findall('channel/item')
newsFile = open('allTags.json', 'w', encoding='utf-8')

allTags = []
for item in items[0]:
    allTags.append(item.tag)

result = []
for i in items:
    result.append({})
    for tag in allTags:
        try:
            result[-1][tag] = i.find(tag).text
        except BaseException:
            result[-1][tag] = 'None'

newsFile.write(json.dumps(result, ensure_ascii=False, separators=(',\n ', ': ')))
newsFile.close()