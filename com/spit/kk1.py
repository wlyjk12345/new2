import requests
from bs4 import BeautifulSoup
def get(page):
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    r = requests.get(url)
    #print(r.text)
    bs = BeautifulSoup(r.text, 'lxml')
    print(bs.find_all(class_ ='name'))


for i in range(1,30):
    get(i)

