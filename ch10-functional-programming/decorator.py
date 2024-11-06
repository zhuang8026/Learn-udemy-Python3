def test1(x, y):
    # print(test1.__name__) # test1
    return x * 2 + y


# test1(1)


def test2(x):
    # print(test2.__name__) # test2
    return x * x * x


# test2(2)


def demo(ff):
    def f_new(*args, **kwargs):
        print("f_new:", ff.__name__)  # 打印出 test1 名字
        # print("args:", args)  # *args 允許你在函數中接收不定數量的「位置引數」
        # print("kwargs:", kwargs)  # **kwargs 允許你在函數中接收不定數量的「關鍵字引數」，也就是 key:value

        return ff(*args, **kwargs)

    return f_new


f = demo(test1)

print("test1:", f(2, 7))  # 11

f = demo(test2)

print("test2:", f(2))  # 8


# 自定義 @demo 裝飾器
# 使用裝飾器就會有 @demo 的特性
@demo
def test3(x):
    return x * 2 * x


a = test3(4)

print("test3:", a)


# 將test3傳給@demo
@demo
def test3(x,y):
    print("hello world ~~~")


# test3() #[ERROR] 請檢查裝飾器本身是否需要傳入參數，如需要傳入參數則需改成 test3(1,2)


# 自定義 @demo_new 裝飾器
def demo_new(s):
    # 定義 @demo 裝飾器
    def demo(f):
        def f_new(*args, **kwargs):
            print(s)
            print(f.__name__)
            return f(*args, **kwargs)

        return f_new

    return demo


@demo_new("hello world")
def test4(x, y, z):
    print("x={}, y={}, z={}".format(x, y, z))

# ff = demo_new("hello world")(test4)
# ff(1, 2, 3)

test4(1, 2, 3)
