"""python基本数据结构示例"""
# 数据和字符串转换
print(chr(65))
print(ord('A'))

print(int('2'))
print(str(2))

""" 字符串包含"""
string = 'helloworld'
if 'world' in string:
    print('Exist')
else:
    print('Not exist')

"""list取值"""
a_list = [1, 2, 3]
print(a_list[0])

"""enumerate函数的使用"""
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)

"""数学运算中常遇的一些错误"""
# RuntimeWarning: invalid value encountered in double_scalars
kss = 0.22917998605606738
kg = 0.832161545953715
period_num_1d = 24
# 开方运算会遇到根式下为负数的情况，会得到复数，如果数据类型是float，那么运算结果会为nan
kss_period = (1 - (1 - (kss + kg)) ** (1 / period_num_1d)) / (1 + kg / kss)
print(type(kss_period))
print(kss_period)

# 基本数学运算符中，整除符号是//
a = 10
b = 5
c = a // b
print("c 的值为：", c)
