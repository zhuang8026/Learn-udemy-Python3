import pdb

pdb.set_trace() # 设置断点

# 如何使用？
# cmd -> enter "python /Users/.../debug_pdb_answer.py(文件路徑)" 
# cmd -> ? (menu 縱覽)
# cmd -> list (預覽程式碼)
# cmd -> step (一步一步執行程式碼)
# cmd -> next (直接執行完成程式碼)
# cmd -> exit (離開程式)


numbers = [1, 2, 3, 4, 10, -4, -7, 0]

def all_even(num_list):

    even_numbers = []
    for number in num_list:
        if number % 2 == 0:
            even_numbers.extend(number)

    return even_numbers


all_even(numbers)
