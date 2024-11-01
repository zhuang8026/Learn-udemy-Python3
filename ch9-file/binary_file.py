# f = open('test6.txt', 'wb') # wb 寫入二進制
# f.write(b'hello world binary') # 寫入 bytes
# f.close()


# i = b'hello world' # bytes 二進制
# print(i.read())
# i.close()

f = open('test6.txt', 'rb') # rb 讀取二進制
print(f.read())
f.close()
