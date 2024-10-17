# 裝飾器

class People:

    def __init__(self, name, age):
        self.__name = name # 私有变量
        self.__age = age # 私有变量

    # @property 是裝飾器，用來把方法轉變為屬性，允許你將屬性設定為私有
    @property
    def name(self):
        # 格式的规范
        return self.__name.upper() # upper() 將字串變成大寫

    @name.setter # 用來代替 setter 方法，控制屬性賦值
    def name(self, name):
        # 做一些合法性的检查
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age


someone = People(name='Jack', age=20)
print(someone.name)
someone.name = 'Test'
print(someone.name)

someone.set_age(30)
print("age1:", someone.get_age())
print("age2:", someone._People__age)