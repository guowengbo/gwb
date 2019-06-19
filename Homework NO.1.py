# Homework 1
import sys
import urllib.request
import urllib.parse
def mylnput(prompt):
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readlinne()

name=mylnput("请输入查询的内容：")
data = urllib.parse.urlencode({'wd':'name'})
print(data)
url = 'http://www.baidu.com/s?' + data
response = urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)


# Homework 2
import urllib.request
import urllib.parse
def toFullPath(sub,parent):
    if isFullPath(sub):
        return sub
    if sub == "/":
        return "http://%s" % (getDomain(parent))
    if sub[:1] == "/":
        baseUrl = getDomain(parent)
    else:
        baseUrl = getBaseUrl(parent)
    relPath = getRelPath(sub)
    return "http://%s/%s" % (baseUrl,relPath)
data = bytes(urllib.parse.urlencode({'pw':'123','acc':'456'}),enconding='utf8')
url = 'http://httpbin.org/post'
response = urllib.request.urlopen(url,data=data)
result = response.read().decode('utf8')
print(result)