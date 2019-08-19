import requests
import time
from bs4 import BeautifulSoup
import os
from multiprocessing import Pool
def get(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }
    url = 'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-' + str(page)
    r = requests.get(url)
    #print(r.text)
    bs = BeautifulSoup(r.text, 'lxml')
    print(bs.find_all(class_ ='name'))

def run_proc(a):
    b = a * 10
    c = b + 10
    for i in range(b,c):
        start = time.time()
        get(i)
        end = time.time()
        print('Task  runs %0.2f seconds.' %  (end - start))

if __name__ == '__main__':  # 批量创建
    print('Parent process %s .' % os.getpid())
    p = Pool()  # 限制
    for a in range(4):
        p.apply_async(run_proc,args=(a,))  # 执行函数和函数
    p.close()
    p.join()