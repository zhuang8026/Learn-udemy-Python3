a = [1, 2, 3]

b = [1, 'abc', 2.0, ['a', 'b', 'c']]


print(a)
print(b)

print(a[0], a[1], a[2], sep='-') # end(結尾),sep(間隔)

c = b[1:3] # index:1和index:3-1 個 >> 1~2

print("testing:", c, type(c))

s = 'abcdef'

print(s[1:3], s[-1]) # bc f

print(b[-1]) # ['a', 'b', 'c']

