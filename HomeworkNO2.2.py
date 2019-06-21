import urllib.request
import http.cookiejar,urllib.request
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
url = 'http://www.17k.com/chapter/2933095/36699279.html'
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
for item in cookie:
    print(item.name,item.value)
    filrname = 'gwb.txt'
    cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)
    cookie = http.cookiejar.MozillaCookieJar()
    cookie.load('gwb.txt')
    print(cookie)