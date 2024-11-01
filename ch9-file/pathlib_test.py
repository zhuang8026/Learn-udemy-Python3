import os
from pathlib import Path, WindowsPath # python 內置模塊，用於處理路徑

# https://docs.python.org/3/library/pathlib.html

# in_file = os.path.join(os.getcwd(), "demo", "test.txt")
# print("files:", in_file) # /Users/.../Learn-udemy-Python3/demo/test.txt

a = Path.cwd() # 當前目錄

print(a)

b = (Path.cwd() / "demo" / "test.txt") # 當前目錄 + demo/test.txt = /Users/.../Learn-udemy-Python3/demo/test.txt

print(type(b))

p = Path.cwd().parent # 當前目錄的上層目錄

for file in p.glob("*"): # 當前目錄的文件路徑打印出來，只找“同層”的文件
    print(file)

for file in p.rglob("*"): # 當前目錄的所有的文件，包括“子”文件
    print(file)

for file in p.rglob("*.txt"): # 當前目錄的所有的txt文件，包括“子”txt文件
    print(file)

# glob, rglob