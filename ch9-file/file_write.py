# r 讀
# w 覆蓋+寫入
# x 創建新文件
# a 保留+寫入
# b 寫入二進制
# t

# example of file write
# f = open("demo1.txt", mode='x')
# f.write("demo1\n")
# f.close()

# example of file write more line
# f = open("demo1.txt", mode='x')
# f.write("demo1\n")
# f.writelines(["demo2\n", "demo3\n"])
# f.writelines(("demo4\n", "demo5\n"))
# f.close()


# f = open("demo1.txt", mode='x')
# f.write("demo1\n")
# f.writelines(["demo2\n", "demo3\n"])
# f.writelines(("demo4\n", "demo5\n"))
# f.close()

# example of file append
# f = open("demo1.txt", mode='a')
# f.write("demo1\n")
# f.writelines(["demo2\n", "demo3\n"])
# f.close()

# example of file write
# f = open("demo1.txt", mode='w')
# f.write("demo1\n")
# f.writelines(["demo2\n", "demo3\n"])
# f.close()

# 中文需加 encoding='utf8'
f = open("test5.txt", mode='w', encoding='utf8')
f.write("第一行\n")
f.close()
