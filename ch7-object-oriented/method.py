# self 指向的是 "实例" 本身
# cls 指向的是 "类" 本身
# 我理解的是 我实例化 10個People，就會有 10個sayhi 方法，但test1() 只有一個

class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))

    # 唯一性
    # 類裝飾器
    @classmethod
    def test1(cls):
        print('这是一个类方法')
        cls.test2()
        # cls.sayhi() # ERROR 因為 sayhi用的是 self 方法

    # 唯一性
    # 靜態方法 不需要帶 self 或 cls
    @staticmethod
    def test2():
        # 静态方法不能访问 self 或 cls，因此不能访问实例或类的属性。
        print('这是一个静态方法')

    def test3():
        print('这是一个普通函数')


p1 = People(name='Jack', age=20)
p2 = People(name='Jack', age=20)

# 呼叫的事p1自身的方法
p1.sayhi()

# 呼叫同一個類的方法
p1.test1()
p2.test1()

# test
# People.test1()
# People.test2()
# People.test3()

# p1 = People(name='Jack', age=20)
# p1.test1()
# p1.test2()
# p1.test3() # [ERROR] 會自帶self, test3 沒有用到self, 所以會報錯