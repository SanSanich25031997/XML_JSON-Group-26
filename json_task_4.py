from urllib.request import urlopen
from json import loads
from itertools import groupby
import json

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))

group = groupby(data['query']['pages']['192203']['revisions'], key=lambda x: x['timestamp'].split('T')[0])
date = ''
maxEdits = 0

for key, item in group:
    editCount = len(list(item))
    if maxEdits < editCount:
        maxEdits = editCount
        date = key

outFile = open('Belmondo.json', 'w', encoding='utf-8')
outFile.write(json.dumps(date + " " + str(maxEdits), ensure_ascii=False, separators=(',\n ', ': ')))
outFile.close()

print('done')

# Этот способ не является надёжным, так как большое количество правок не всегда означает смерть.
