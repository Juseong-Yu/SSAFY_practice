# 아래 함수를 수정하시오.
def add_item_to_dict(dictionary, key, value):
    new_dict = dictionary.copy()
    add_dict = {key : value}
    new_dict.update(add_dict)
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
