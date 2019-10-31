import requests

r = requests.get('https://www.baidu.com')
print(r.cookies)
for key, target_directory in r.cookies.items():
    print(key + '=' + target_directory)

requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)