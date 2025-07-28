# 아래 함수를 수정하시오.
def find_min_max(lst):
    max_num = max(lst)
    min_num = min(lst)
    return (min_num, max_num)


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
