import functools


def demo(f):

    @functools.wraps(f) # 保留原始函數屬性(__name__, __doc__ ....)
    def f_new(*args, **kwargs):
        """
        this is 'f_new'
        :param args:
        :param kwargs:
        :return:
        """
        print(f.__name__)
        return f(*args, **kwargs)
    return f_new


@demo
def test1(x, y):
    """
    this is 'test1'
    :param x:
    :param y:
    :return:
    """
    print('x={}, y={}'.format(x, y))


print(test1.__name__) # test1

print(test1.__doc__) # this is test1...
