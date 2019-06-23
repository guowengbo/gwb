import urllib.request
import socket
import urllib.error
URLS = []
url = 'http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML = response.text
try:
    response = urllib.request.urlopen('http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808',timeout=0.1)
except urllib.error.URLError as url:
    if isinstance(url.reason,socket.timeout):
        print('timeout')
for url in URLS:
    response = requests.get(url)
    content = response.content
    name = url.split('/')[-1]
    with open(name,'wb') as f:
        f.write(content)
    