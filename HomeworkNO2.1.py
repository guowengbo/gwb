import urllib.request
url = 'http://www.baidu.com'
proxy_handle = {
    'http':'183.51.190.51:33913',
    'http':'122.193.245.44:9999'
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
request = urllib.request.Request(url=url)
response = urllib.request.urlopen(request)
print(response.read().decode('utf8'))
while 1:
    print(response.status)   
    if (response.status != 200):
        print('爬虫失败')
    break



