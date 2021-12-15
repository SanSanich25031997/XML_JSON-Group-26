from urllib.request import urlopen
from json import loads
from itertools import groupby

url = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
data = loads(urlopen(url).read().decode('utf8'))

zz = groupby(data['query']['pages']['192203']['revisions'], key= lambda x:x['timestamp'].split('T')[0])
date=''
max=0
for key, item in zz:
    tem=len(list(item))
    if max<tem:
        max=tem
        date=key
print(date+" "+str(max))

#Этот способ не является надёжным, так как большое количество правок не означает смерть.
