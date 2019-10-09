print("#---------------closure------------------")


# ---------------------闭包的一些基本点------------------------------
def outer():
    var = 3

    def inner():
        print("the func is used: var=" + str(var))

    return inner


# 以上，函数inner和自有变量var的“引用”共同构成了闭包。var对于inner来说是自由变量。
# 在一个内部函数中，对外部作用域的变量进行引用，并且外部函数的返回值为内部函数，那么内部函数就被认为是闭包。
outer()  # no print
func = outer()
func()  # print 3
var = 5
func()  # print 3


# --------------闭包的作用----------------
# 闭包的作用可以保存当前的运行环境
def create(pos=[0, 0]):
    def go(direction, step):
        new_x = pos[0] + direction[0] * step
        new_y = pos[1] + direction[1] * step
        pos[0] = new_x
        pos[1] = new_y
        return pos

    return go


player = create()
print(player([1, 0], 10))
print(player([0, 1], 20))
print(player([-1, 0], 10))

print("--------------------__call__()----------------------------")


# __call__函数的作用
# /usr/bin/env python
class test:
    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        c = self.a + b
        print(c)

    def display(self):
        print(self.a)


Test = test("This is test!")
Test.display()  # 调用display函数
Test("##Append something")  # __call__实际上是将一个类重载了"()"，也就是让一个类也可以像一个函数一样可以拿来调用了。因此这里会调用__call__函数
