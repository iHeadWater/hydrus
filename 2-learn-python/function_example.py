# python函数的相关特点

# ---------------------------回调函数示例-------------------------------------


import time


def apply_async(func, args, *, callback):
    """回调函数的应用，python的函数很灵活，可以直接做函数参数"""
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print('Got:', result)


def add(x, y):
    return x + y


apply_async(add, (2, 3), callback=print_result)

apply_async(add, ('hello', 'world'), callback=print_result)

# ------------all()函数----------------

print(all(['a', 'b', 'c', 'd']))  # 列表list，元素都不为空或0
print(all(['a', 'b', '', 'd']))
print(all([0, 1, 2, 3]))
print(all([]))
print(all(()))

# ------------------eval()函数-----------------------
x = 7
# eval(expression[, globals[, locals]])用来执行一个字符串表达式，并返回表达式的值。
print(eval('3*x'))
print(eval('2+2'))
print(eval('pow(2,2)'))

# ---------------------时间函数-----------------------------
# time的time函数开始计时的时间戳也是1970纪元，返回的是当前时间的时间戳
print("time.time(): %f " % time.time())
print(time.localtime(time.time()))
print(time.asctime(time.localtime(time.time())))
