# 私有屬性

class People:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._protect_var = 10 # 保护变量（內外部都可访问 & 修改）
        self.__private_var = 10 # 私有变量（外部不可直接访问）

    def sayhi(self):
        print("Hi, my name is {}, and I'm {}".format(
            self.name, self.age
        ))

    def get_var(self):
        print(self.__private_var)

    def set_var(self, var):
        self.__private_var = var


someone = People(name='Jack', age=20)

# 基本用法
# someone.sayhi()
# someone.age = 30
# someone.sayhi()

# 保護變數
# someone._protect_var = 30
print(f"_protect_var: {someone._protect_var}")


# 私有變數
# someone.__private_var #【ERROR】
# print(f"__private_var: {someone.__private_var}") #【ERROR】
# someone.get_var() #【success】
# someone.set_var(30) #【success】
# someone.get_var() #【success】

# print(dir(someone)) # 能找到 _People__private_var 是能访问到的__private_var的方法
# someone._People__private_var
print("_People__private_var:", someone._People__private_var)
# someone.get_var()