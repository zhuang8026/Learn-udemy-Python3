# print('hello world', 'python', sep='%', end='.')

# import sys
#
# sys.stdout.write('hello world%python.')


# a = input('ddddddddd:')
# print(a, type(a)) # <class 'str'>

import sys

a = sys.stdin.readlines() # list, 需要輸入 Ctrl+D 才會結束

print(a, type(a)) # <class 'list'>
