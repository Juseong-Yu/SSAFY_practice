# 아래 함수를 수정하시오.
def sort_tuple(lst):
    new_tuple = list(lst)
    new_tuple.sort()
    new_tuple = tuple(new_tuple)
    pass
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
