def func_demo(a, b):
    # """ + doc + """ -> 是用來描述函數的用途 
    # func_demo.__doc__ -> 會出現 doc string

    """ doc test demo
    >>> func_demo(1, 2)
    3
    >>> func_demo('a', 'b')
    'ab'
    >>> func_demo([1, 2], [3, 4])
    [1, 2, 3, 4]
    >>> func_demo({1:1}, {2:2})
    False
    >>> func_demo(1, '2')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    >>>
    """
    if isinstance(a, dict):
        return False
    return a + b

# 文檔測試方法
if __name__ == "__main__":
    import doctest
    doctest.testmod() # 會執行 ">>>" 所有的的測試內容 
