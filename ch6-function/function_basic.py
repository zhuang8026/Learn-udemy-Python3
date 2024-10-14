# a = [1, 2, 3, 4]
#
# print(max(a))


def demo():
    print('hello world')
    print('demo')


def demo1(a, b):
    print(a, b)


def sum(a, b):
    return a + b

print("sum:", sum(a = [1,2,3], b = [1,2,3]))
print("sum:", sum(a = [1,2,3], b = [1,2,3]))
print("sum number is {}".format(sum(a = [1,2,3], b = [1,2,3])))

def my_max(a):
    if not a:
        return None
    max_value = a[0]
    for item in a:
        if item > max_value:
            max_value = item
    return max_value

a = [1, 4, 5, 2,3,8,10]

print(my_max(a))
