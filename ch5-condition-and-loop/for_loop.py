
a = '12345'

b = [1, 2, 3, 4]

c = ('a', 'b', 'c', 'd')

d = {
    1: 'a',
    2: 'b',
    3: 'c'
}

e = {1, 2, 3, 5, 9}

for (key, value) in d.items():
    print('{}={}'.format(key, value))

# for item in e:
#     print(item)

for item in range(1, 20): # -> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
    print(item)
