# 아래 함수를 수정하시오.
def get_keys_from_dict(dictionary):
    keys = list(dictionary.keys())
    return keys

def get_all_keys_from_dict(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    for value in values:
        if isinstance(value, dict):
            key = get_all_keys_from_dict(value)
            keys.extend(key)
    return keys

my_dict = {'name': 'Alice', 'age': 25}
result = get_keys_from_dict(my_dict)
print(result)  # ['name', 'age']

my_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': 'NY'}
result = get_all_keys_from_dict(my_dict)
print(result)  # ['person', 'name', 'age', 'location']
