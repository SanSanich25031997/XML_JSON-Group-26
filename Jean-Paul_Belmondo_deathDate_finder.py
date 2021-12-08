from urllib.request import urlopen
from json import loads
from itertools import groupby

url = 'https://ru.wikipedia.org/w/api.php?' \
      'action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0' \
      '%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE,_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C '
data = loads(urlopen(url).read().decode('utf8'))

sortedData = groupby(data['query']['pages']['192203']['revisions'],
                     key=lambda x: x['timestamp'].split('T')[0])
maxRevisions = 0
foundDate = ''

for key, item in sortedData:
    y = len(list(item))
    if maxRevisions < y:
        maxRevisions = y
        foundDate = key
print(foundDate + " " + str(maxRevisions))  # 2021-09-06 58

# Этот способ не является рабочим должным образом, потому что статья может быть написана про человека, который жил
# ещё до появления Интернета, а значит, уже был мёртв на момент написания статьи. Информация с течением времени могла
# измениться в силу новых исторических открытий, связанных с темой статьи Википедии. А значит, искать информацию по
# большему количеству правок имеет смысл лишь в случае тех событий, что происходят уже в эпоху Интернета либо имеют
# влияние на события наших дней (например, корректировка исторических данных движением BLM).
