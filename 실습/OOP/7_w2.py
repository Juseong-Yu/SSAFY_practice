# 아래 클래스를 수정하시오.
class StringRepeater:
    @staticmethod
    def repeat_string(n, string):
        for _ in range(n):
            print(string)
    pass


repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
