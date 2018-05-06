import os
import shutil as sh
from urllib.request import urlopen
from bs4 import BeautifulSoup

# YouTube playlist URL - youtube show 200 max in playlist

page_url1 = 'https://www.youtube.com/watch?v=qVdxj8XOB00&index=201&list=PLAwxTw4SYaPlqMkzr4xyuD6cXTIgPuzgn'
page_url2 = 'https://www.youtube.com/watch?v=-fpVTLGoxZ4&list=PLAwxTw4SYaPlqMkzr4xyuD6cXTIgPuzgn&index=301'
page_url3 = 'https://www.youtube.com/watch?v=SQ-b40cVia8&list=PLAwxTw4SYaPlqMkzr4xyuD6cXTIgPuzgn&index=401'
page_url4 = 'https://www.youtube.com/watch?v=T57JLskDv7g&list=PLAwxTw4SYaPlqMkzr4xyuD6cXTIgPuzgn&index=501'
page_url5 = 'https://www.youtube.com/watch?v=lzJsHUVKvRc&list=PLAwxTw4SYaPlqMkzr4xyuD6cXTIgPuzgn&index=601'
page_url6 = 'https://www.youtube.com/watch?v=o7IiWAz3Jes&index=701&list=PLAwxTw4SYaPlqMkzr4xyuD6cXTIgPuzgn'
page_url7 = 'https://www.youtube.com/watch?v=Y6LF-_-pMgI&list=PLAwxTw4SYaPlqMkzr4xyuD6cXTIgPuzgn&index=801'

url_list = [page_url1,page_url2,page_url3,page_url4,page_url5,page_url6,page_url7]

# Extracting data from these URLs

for url in url_list:
    page = urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    raw_data = soup.find_all('h4', {'class':'yt-ui-ellipsis'})

    t_file = open('/home/yewaiyanoo/udacityAI.txt','a')
    
    for x in raw_data:
        t_file.write(str(x))
        

# Filenames from my drive

filelist = os.listdir('/media/yewaiyanoo/Excellent/Intro to Artificial Intelligence')

t_file = open('/home/yewaiyanoo/udacityAI.txt','r')

t_list = list(t_file)

t_file.close()

title = [x.replace('\n','').strip() for x in t_list]

title_list = []

for x in title:
    if len(x) > 2:
        title_list.append(x)

os.chdir('/media/yewaiyanoo/Excellent/Intro to Artificial Intelligence')
         
for t in range(len(title_list)):
    for j in filelist:
        if title_list[t] == j[:-4]:
            print(j,"file has been changed for sorting...")
            os.utime(j,(t,t))

    print(t)  
                      
