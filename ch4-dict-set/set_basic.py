# 集合的创建

a = {'a', 'b', 'c'} # 集合

b = {
    'a': 1,
    'b': 2,
    'c': 3
} # 字典
print(type(a))


# 集合的使用

t = 'd' in a

print(t)

x = 'a' in b
print(x)


l = [1, 2, 3, 2, 4, 5, 2] # 列表

s1 = set(l) # 集合 -> {1, 2, 3, 2, 4, 5, 2}

print(s1, type(s1), list(s1)) # {1, 2, 3, 4, 5} <class 'set'> [1, 2, 3, 4, 5]

