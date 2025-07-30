# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def print_info(self):
        print('Width:',self.width)
        print('Height:',self.height)
        print('Area:',self.width * self.height)
        print('Perimeter',self.height * 2 + self.width * 2)
        pass


shape1 = Shape(5, 3)
shape1.print_info()
