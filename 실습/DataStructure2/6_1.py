# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    return set1 | set2

def union_multiple_sets(*sets):
    if len(sets) < 2 :
        return "최소 두 개의 셋이 필요합니다."
    else:
        result = set()
        for set_check in sets:
            result = result | set_check
        return result


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
print(result)
# 출력 : 최소 두 개의 셋이 필요합니다
