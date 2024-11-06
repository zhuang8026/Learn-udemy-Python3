# lambda匿名函数


# 一般寫法
def test(x, y):
    return x + 2 * y


print(test(1, 2))

# lambda寫法 (會return資料)
f = lambda x, y: x + 2 * y
print(f(1, 2))

# 以上是一樣的結果


# 如何使用lambda?
def demo(x, y, f):
    # x, y = 1, 2
    # f = lambda function
    return f(x, y)


print(demo(1, 2, lambda x, y: x + 2 * y))


def add_n(n):
    return lambda x: n + x


f = add_n(40)  # f = lambda x: 40 + x

print(f(1))  # f = lambda 1: 40 + 1 / QA：41
print(f(-10))  # f = lambda -10: 40 + -10 / QA：30
