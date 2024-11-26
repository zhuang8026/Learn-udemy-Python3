class A:
    pass


class B(A):
    pass


class C:
    pass


a = A()  # a是A類別的實例

b = B()  # B是A的子类

# isinstance
# 用法：isinstance(物件, 類別)
# 功能：判斷物件是否為指定類別的實例 || 子類別的實例

print(isinstance(a, A))  # True
print(isinstance(a, B))  # False
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True
print("c->", isinstance(b, (A, B, C))) # 說明：b 是否為 A or B or C 的實例 || 子類別的實例 
                                        # True
# isinstance(b, A) or isinstance(b, B) or isinstance(b, C)
