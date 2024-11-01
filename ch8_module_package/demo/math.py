# 模块 module
# 這是一個模塊，並且有許多方法在其中

def my_sum(*args):

    result = 0
    for item in args:
        result += item

    return result


def my_max(*args):
    print("最大值")


def my_min(*args):
    print("最小值")


class People:

    def __index__(self, name, age):
        self.name = name
        self.age = age


MAX_NUM = 100

print("__name__：", __name__) # ch8_module_package.demo.math


if __name__ == '__main__':
    # 單獨允許此文件，才會出現一下內容
    print('1+2+3+4 =', my_sum(1, 2, 3, 4))
