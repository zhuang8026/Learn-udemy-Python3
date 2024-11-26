from collections import deque

# deque 是雙向队列，顧名思義就是可以對他的首端和末端進行操作
d = deque([1, 2, 3])

d.append(4)  # 將 數字 加入到末端
print(d)  # [1, 2, 3, 4]
d.appendleft(0)  # 將 數字 加入到首端
print(d)  # [0, 1, 2, 3, 4]

d.pop()  # 將末端移除
print(d)  # [0, 1, 2, 3]
d.popleft()  # 將首端移除
print(d)  # [1, 2, 3]


d.extend([4, 5])  # 擴展 -> 將 列表 加入到末端
print(d)  # [1, 2, 3, 4, 5]
d.extendleft([0, -1, -2])  # 擴展 -> 將 列表 加入到首端
# 注意：插入順序是從0開始，所以 0 進入 "[0, 1, 2, 3, 4, 5]"，-1進入 [-1. 0, 1, 2, 3, 4, 5]
print(d)  # [-2, -1. 0, 1, 2, 3, 4, 5]

d.reverse() # 反轉
print(d)  # [5, 4, 3, 2, 1, 0, -1]

d.insert(0, 123) # 插入(指定位置, 插入參數)
print(d)  # [123, 5, 4, 3, 2, 1, 0, -1]
