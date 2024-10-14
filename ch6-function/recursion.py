# n! = 1*2*3........(n-1)*

# n* (n-1) * (n-2)...........2*1!

def test(n):
    result = 1
    for item in range(1, n+1): # range(1, n+1) = 1 2 3
        result = result * item # 1x1 1x2 2X3
        print(result, item)
    return result

print(test(3))

# def test(n):
#     if n == 1:
#         return n
#     return n * test(n-1)


# print(test(3))
