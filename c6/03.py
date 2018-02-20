from urllib.request import urlopen
from xml.etree.ElementTree import parse

u = urlopen('http://python3-cookbook.readthedocs.io/zh_CN/latest/c06/p03_parse_simple_xml_data.html')
u = urlopen('http://planet.python.org/rss20.xml')
doc = parse(u)

for item in doc.iterfind('channel/item'):
    title = item.findtext('title')
    date = item.findtext('pubDate')
    link = item.findtext('link')
    print(title)
    print(date)
    print(link)
    print()
