import urllib.request
import urllib.parse
import ssl

url = 'http://www.baidu.com'

response = urllib.request.urlopen('http://www.baidu.com')
#  urllib.request.urlopen(url, data=None, [timeout, ]*)
print(response.read().decode('utf-8'))


headers = {
    # 假装自己是浏览器
    'User-Agent': ' Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
dict = {
    'return_url':'https://biihu.cc/',
    'user_name':'xiaoshuaib@gmail.com',
    'password':'123456789',
    '_post_type':'ajax',
}

data = bytes(urllib.parse.urlencode(dict),'utf-8')

req =  urllib.request.Request(url,data=data,headers=headers,method='POST')
# urllib.request.Request(url, data=None, headers={}, method=None)

response =  urllib.request.urlopen(req)
print(response.read().decode('utf-8'))