
# def add(a, b):
#     return a + b


# def add(*args):
#
#     result = 0
#     for item in args:
#         result += item
#     return result
#
#
# print(add(1, 2, 10, 20, 30))
#

# def test(a, b, c):
#     print(a + b + c)
#
# 
# **kwargs 是一種特殊的語法，用來接收 “不定數量” 的關鍵字參數
# def add(x, **kwargs): 
#
#     if x == 2:
#         test(**kwargs)
#
#
# add(x=2, a=1, b=2, c=2)
#

def test(a, b=False):
    if b:
        return a
    else:
        return a * a


print("test:", test(a=2, b=True))


def test123(**kwargs):
    pass


def example_mixed(a, *args, **kwargs):
    print(f"普通參數: {a}")
    print(f"位置參數: {args}")   # 結果: (20, 30)
                                # 傳入的是 tuple (tuple 不可變，list 可變)
    print(f"關鍵字參數: {kwargs}") #結果: {'name': 'Alice', 'age': 25}
                                #傳入的是 dict (key: value) 

example_mixed(10, 20, 30, name="Alice", age=25)