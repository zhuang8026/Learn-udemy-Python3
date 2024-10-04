d = {
    'Name': 'Jack',
    'Age': 9,
    'Grade': 5,
}

print(d.get("name"))
print(d['Age'])


print("keys->", d.keys())
print("keys->", list(d.keys())) # list(...) 函數將任何可迭代對象（如字典視圖）轉換為列表。

print(d.values())

print(d.items())

c = d.pop('Name') #刪除指定數據 並 取出來

print(c) # Jack

print(d) # { 'Age': 9, 'Grade': 5 }

d.clear() # 清空字典

print(d)  # {}


# 字典的更新

c = {
    1: 1,
    2: 2
}

c[3] = 3
c[4] = 4

print(c)


d = {
    1: 5,
    6: 6
}

# c.update(d)
#
# print(c)

e = {**c, **d} # 合併

print(e)



