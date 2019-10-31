import urllib.parse
import urllib.request

# 以 Python 官网为例，我们来把这个网页抓下来：
response = urllib.request.urlopen('https://www.python.org')
print(response.read().decode('utf-8'))

# 利用 type() 方法输出 Response 的类型。通过输出结果可以发现它是一个 HTTPResposne 类型的对象
print(type(response))

# 得到这个对象之后，我们把它赋值为 response 变量，然后就可以调用这些方法和属性，得到返回结果的一系列信息了。
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))

# 想给链接传递一些参数该怎么实现呢？我们首先看一下 urlopen() 函数的API：
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())

# timeout 参数可以设置超时时间，单位为秒，意思就是如果请求超出了设置的这个时间还没有得到响应，就会抛出异常，如果不指定，就会使用全局默认时间。它支持 HTTP、HTTPS、FTP 请求。
response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# 在这里我们设置了超时时间是 1 秒，程序 1 秒过后服务器依然没有响应，于是抛出了 URLError 异常，它属于 urllib.error 模块，错误原因是超时。
print(response.read())