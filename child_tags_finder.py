import xml.etree.ElementTree as ET
from urllib.request import urlopen
import json

data = urlopen('https://lenta.ru/rss').read().decode('utf8')
root = ET.fromstring(data)
items = root.findall('channel/item')
f = open('data.json', 'w', encoding='utf-8')
for i in items:
    f.write(json.dumps([i.find("pubDate").text, i.find("title").text], ensure_ascii=False) + '\n')

print('The work is done!')
