from collections import OrderedDict
#基本上 OrderedDict 和 dict 一模一樣，但 OrderedDict 可以保證我們賦值的順序

c = dict()

c['a'] = 1
c['c'] = 3
c['b'] = 2
c['d'] = 4

print(c) # python2.6 之前版本，dict賦值的時候，顯示順序不一定會按照我們設定的順序，所以才要用OrderedDict
        # result: {'a': 1, 'c': 3, 'b': 2, 'd': 4}
d = OrderedDict()
d["a"] = 1
d["b"] = 2
d["c"] = 3

print(d) # result: OrderedDict([('a', 1), ('b', 2), ('c', 3)])

d.move_to_end("a") # 將 "a" 移動到字典的最後一個

print(d) # result: OrderedDict([('b', 2), ('c', 3), ('a', 1)])
