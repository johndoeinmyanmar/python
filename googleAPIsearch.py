from urllib import request
from bs4 import BeautifulSoup
import sys

urls = []
urls2 = []

tarurl = sys.argv[1]

url = request.urlopen(tarurl).read()
soup = BeautifulSoup(url)

for line in soup.find_all('a'):
    newline = line.get('href')
    try:
        if newline[:4] == "http":
            if tarurl in newline:
                urls.append(str(newline))
                
        elif newline[:1] == "/":
            combine = tarurl+newline
            urls.append(str(combine))
    except:
        pass

    for uurl in urls:
        url = request.urlopen(uurl).read()
        soup = BeautifulSoup(url)
        for line in soup.find_all('a'):
            newline = line.get('href')
            try:
                if newline[:4] == 'http':
                    if tarurl in newline:
                        urls2.append(str(newline))
                elif newline[:1] == '/':
                    combine = tarurl + newline
                    urls2.append(str(combine))
            except:
                pass

            urls3 = set(urls2)

    for value in urls3:
        print(value)
            
                        
