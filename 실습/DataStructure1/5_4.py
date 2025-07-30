# 아래 함수를 수정하시오.
def capitalize_words(words):
    words = words.split(' ')
    result = []
    for word in words:
        word = word.capitalize()
        result.append(word)
    return ' '.join(result)


result = capitalize_words("hello, world!")
print(result)
