# urlparser

from urllib.parse import urlparse

url = 'http://www.python.org:80/guido/python.html;philosophy?a=10&b=20#here'
result = urlparse(url)
print(result)