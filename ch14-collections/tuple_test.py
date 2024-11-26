# tuple

print("1.iterable")
my_tuple = ("python", 3, 7, 3)  # 元组 -> 結構&資料不可變
for i in my_tuple:
    print(i)

print("2.indexing and slicing")
print(my_tuple[0])
print(my_tuple[0:2])

print("3.sequence unpacking")
name, _, y, z = my_tuple  #  _ 用來忽略
print(name, y, z)  # name=python, y=7, z=3

name, *_ = my_tuple  # *_ 用來忽略index為0後面的所有值
print(name)  # name=python

name, *version = my_tuple
print(name, version)  #  name=python, version=[3, 7, 3] version 會是一個list


print("4.immutable")
# my_tuple[1] = 2  [ERROR] 元组 -> 不可變結構、資料

my_dict = {my_tuple: 1}  # 元组 -> {key:value}
print(my_dict)  # { ('python', 3, 7, 3): 1 }

my_tuple = (1, 2, 3)  # 重新創建元祖
print(my_dict)  # 和29行新創建的元祖沒有關係 -> { ('python', 3, 7, 3): 1 }

# my_dict = {[1, 2]: 1} # [ERROR] 注意：作為索引 key 必須是不可變的，[1, 2]是list，list可變

# i = 1
# a = {i: 1}
# i = 2
# print(a)

a = []  # 資料、結構可變

b = ()  # 資料、結構不可變
