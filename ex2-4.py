# http.client.HttpConnection를 사용한 GET 방식 요청

from http.client import HTTPConnection

conn = HTTPConnection('www.example.com')
conn.request('GET', '/')

result = conn.getresponse()
print(result.status, result.reason)

data = result.read()
print(data)