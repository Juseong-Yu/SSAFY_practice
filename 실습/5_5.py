# 아래 함수를 수정하시오.
def even_elements(my_list):
    even = []
    for _ in range(len(my_list)):
        if my_list[0] % 2 != 0:
            my_list.pop(0)
        else:
            my_list.extend([my_list.pop(0)])
    return my_list
            


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
