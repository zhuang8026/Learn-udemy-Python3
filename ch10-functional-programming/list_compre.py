a = [1, 2, 3, 4]

# b = [2, 3, 4, 5]

# 列表解析

# b = [item for item in a] # -> [1 2 3 4]
b = [item for item in a if item % 2 == 0] # -> [2 4]
# for item in ... 並不會返回任何值
print(b) # [1, 4, 9, 16]

# 字典解析
dd = {'a': 1, 'b': 2, 'c': 3}
# 创建一个新字典，将原字典的值翻倍
new_dict = { key: value * 2 for key, value in dd.items() if value != 1 }  
print(new_dict) # {'b': 4, 'c': 6} 
