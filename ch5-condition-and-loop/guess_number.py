import random

a = random.randint(0, 100) # 生成一個數字 (randint 隨機)


while True:
    num = int(input("请输入一个0-100之间的数字：")) # 用戶輸入數字
    if num == a:
        print("恭喜您，猜对了！")
        break
    elif num > a:
        print("猜大了，请重新猜！")
    else:
        print("猜小了，请重新猜！")
