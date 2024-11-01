f = open('test4.txt', mode='r', encoding='utf8')

# a = f.read()
# print(a, type(a)) # str
# f.close()

# for line in f:
#     print(line)

# a = f.readlines() # list, 因為會一次讀取全部，效能方面會比較差
# b = f.readline() # str, 每次只讀一行
#
# print(a, type(a))
# print(b, type(b))


# print(f.readline())


for line in f:
    print(line) # 會跑出 line1 line2 line3

for line in f:
    print(line) # 因為上面已經讀完了，所以會跑出空值

f.close()
