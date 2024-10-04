# 获取列表的一些基本信息

list1 = [9, 1, -4, 3, 7, 11, 3]

print('list1的长度 =', len(list1)) # list長度


print('list1里的最大值=', max(list1)) # 最大值11


print('list1里的最小值 =', min(list1)) # 最小值11


print('list1里3这个元素一共出现了{}次'.format(list1.count(3))) # 數字3 出現過幾次


# 列表的改变

list2 = ['a', 'c', 'd']

# 给list2结尾添加一个新元素 'e'

list2.append('e')
print('list2=', list2)

 
# 在list2的'a'和'c'之间插入一个 'b'
list2.insert(1, 'b')
print('list2=', list2)

# 删除list2里的'b'
list2.remove('b')
print('list2=', list2)


list2[0] = '1'
print('list2=', list2)


# a = '123';  // 
# a[0] = 'a'; // 不能單獨修改字串中的特定文字
# a = 'abc';  // 可以全部替換


# 列表翻转
list3 = [1, 2, 3]
list3.reverse(); #順序反轉，從後往前 or 從前往後
print('list3=', list3)


# 列表排序

list4 = [9, 1, -4, 3, 7, 11, 3]
list4.sort(reverse=True)
# sort 正常排序
# sort(reverse=True) 變成倒序
print('list4=', list4)


list5 = [1, 'a', 3, [1,2], 'c']
# list5.sort(); # failed (不可用，因為會比對元素的類型)
# list5.reverse(); # ok (只是顛倒順序，不會比對元素的類型)
list5.insert(1, 'b'); # ok
print('list5 =', list5)

a = [1, 2, 3, 4];
b = a*2;
c = b + [4, 5, 6];
print(b);
print(c);


