a = [1, 2, 3, 4]


# def f(x, y):
#     return x + y

b = map(lambda x: x * x, a)
print(b) # <map object at 0x000001F3F7B9B0A0>
for item in b:
    print(item) # 1 4 9 16

# map(function, iterable)
c = [item for item in map(lambda x: x * x, a)] # 分別將 1,2,3,4 丟入x,並執行完lambda後回傳，然後再繼續下一個
# for item in ... 並不會返回任何值，它只是依次將 map(...) 中的元素取出並分配給 item 變數
print(c)


# 引用 functools 模組 -> 呼叫 reduce
from functools import reduce

# reduce(function, iterable)
s = [1, 2, 3, 4]
ss = reduce(lambda x, y: x + y, s)
#
print(ss)

# filter(function, iterable)
# yy = filter(lambda x: x % 2 == 1, s)

# print( [ item for item in filter(lambda x: x % 2 == 1, s) ] )

# print([item for item in s if item % 2 == 1])