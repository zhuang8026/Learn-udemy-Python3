# 引入 系統路徑

import sys

# print(sys.path)

# 將 系統路徑 加入 sys.path (不指定路徑，會無法使用自己的模塊)
if '/Users/william.chuang/Downloads/Project/Python/Learn-udemy-Python3' not in sys.path:
    sys.path.append('/Users/william.chuang/Downloads/Project/Python/Learn-udemy-Python3')

# 自己寫的模塊
from ch8_module_package.demo.math import my_sum # SUCCESS
# from demo.math import my_sum # SUCCESS
# from 文件夾名.模塊名.方法名 import 方法名

# my_sum 是demo中寫好的
print(my_sum(1, 2, 3, 4))


# if __name__ == "__main__":
#     pass
