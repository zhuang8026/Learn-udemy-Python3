# 元组的创建

a = (1, 2, 3)

b = [1, 2, 3],

print(a, type(a)) # (1, 2, 3)
print(b, type(b)) # ([1, 2, 3],)

# 元组 (tuple) 的访问
# read only -> Yes
# edit -> NO
# delete -> NO
print(a[1])

print(a[1:])  #index1 ~
print(a[1:3]) #index1 ~ index3-1

print(a[-1]) #index end
