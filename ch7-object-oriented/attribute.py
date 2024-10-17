class Student:

    count = 0

    def __init__(self, name):
        Student.count += 1
        self.name = name
        self.__age = 999


s1 = Student('A')
s2 = Student('B')
s3 = Student('C')

print(s1.__age) # [ERROR] 因為是私有變量，所以無法被外部讀取
s1.__age = 888
print(s1.__age) # [SUCCESS] 因為你有複製一個全新的"__age"給s1，和原本的"__age"完全沒有任何關聯

print(Student.count) # 直接引用類變量
print(s1.count) # 如果s1本身沒有該屬性,則會引用類變量,如果s1有該屬性,則是會成為實例屬性

# print(Student.count)
#
# s1 = Student(name='A')
# print(s1.name)
# print(s1.count)
#
# s1.name = 'B'
# s1.count = 1
# print(s1.name)
# print(s1.count)
# print(Student.count)
#
# Student.count = 2
#
#
# print(Student.count)
# print(s1.count)
#
# #########################
#
#
# s2 = Student('X')
#
# print(s2.count)
