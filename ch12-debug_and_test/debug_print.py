numbers = [1, 2, 3, 4, 10, -4, -7, 0]


def all_even(num_list):

    even_numbers = []
    for num in num_list:
        print('num=', num)
        if num % 2 == 0:
            print('发现偶数, number=', num)
            even_numbers.extend([num])

    return even_numbers


print('all even number', all_even(numbers)) # [2, 4, 10, -4, 0]
