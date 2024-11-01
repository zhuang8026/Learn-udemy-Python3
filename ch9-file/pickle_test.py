
class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))

# 序列化对象的寫入與保存
# import pickle # 序列化对象

# p1 = People(name='Jack', age=30) # 創建一個 People 的實例
# f = open('p1', 'wb') # 要往文件python的對象，必須有二進制 (wb 讀取二進制)
# pickle.dump(p1, f) # dump(python對象, 文件)
# f.close()


# 序列化对象的加载
import pickle

f = open('p1', 'rb') # open(文件, 讀取模式)
load_p1 = pickle.load(f) # load(文件)
f.close()

print(load_p1, load_p1.name, load_p1.age) # load_p1 是 People 的實例
load_p1.sayhi() # 呼叫People的sayhi方法

