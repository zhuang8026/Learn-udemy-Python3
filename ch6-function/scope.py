# x = 1
#
# x += 1
#
# print(x)
#
#
# def demo(a):
#     a = a + 10
#     print(a)
#
# demo(a=x)
#
# print(x)


# y = [1, 2, 3]
#
# print(y)
#
#
# def demo1(a):
#     a = a + [4]
#     # a.append(4)
#     print(a)
#
#
# demo1(a=y)
#
# print(y)


z = 1

print(z)


def demo2(a):
    global z # global 是聲明 z 是全域變數，並非區域變數
    z = z + a
    print(z)


demo2(a=10)

print(z)
