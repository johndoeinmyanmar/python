import requests
import re
from bs4 import BeautifulSoup
import sys

if len(sys.argv) != 2:
    print("Usage: %s targeturl" %(sys.argv[0]))
    sys.exit(0)

urls = []

tarurl = sys.argv[1]
url = requests.get(tarurl)
comments = re.findall(r'<--(.*)-->', url.text)
print("Comments on page: " + tarurl)

for comment in comments:
    print(comment)


soup = BeautifulSoup(url.text,"lxml")
for line in soup.find_all('a'):
    newline = line.get('href')
    try:
        if newline[:4] == 'http':
            if tarurl in newline:
                urls.append(str(newline))
        elif newline[:1] == '/':
            combine = tarurl+newline
            urls.append(str(combine))
    except:
        pass
        print("failed...")

for uurl in urls:
    print("Comments on page: " +uurl)
    url = requests.get(uurl)
    comments = re.findall(r'<--(.*)-->', url.text)
    for comment in comments:
        print(comment)
