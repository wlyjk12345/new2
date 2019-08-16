
from bs4 import BeautifulSoup
import requests
#import lxml
'''html_doc = """

<html><head><title>学习python的正确姿势</title></head>
<body>
<p class="title"><b>小帅b的故事</b></p>

<p class="story">有一天，小帅b想给大家讲两个笑话
<a href="http://example.com/1" class="sister" id="link1">一个笑话长</a>,
<a href="http://example.com/2" class="sister" id="link2">一个笑话短</a> ,
他问大家，想听长的还是短的？</p>

<p class="story">...</p>

"""

soup = BeautifulSoup(html_doc,'lxml')
print(soup.a)
#学习python的正确姿势   '''
for page in range(0,10):
    i = page * 25
    url =  'https://movie.douban.com/top250?start=' + str(i) +  '&filter='
    html =requests.get(url)
    soup = BeautifulSoup(html.text, 'lxml')
    #print(html.text)
    list = soup.find_all('li')
    for item in list:
        item_name = item.find(class_='title').str
        print(item_name)
