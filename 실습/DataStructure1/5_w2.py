# 아래 함수를 수정하시오.
def count_character(string, letter):
    count = list(string).count("o")
    return count

result = count_character("Hello, World!", "o")
print(result)  # 2
