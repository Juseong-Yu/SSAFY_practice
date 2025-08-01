# 아래 클래스를 수정하시오.
class Animal:
    num_of_animal = 0

    def __init__(self):
        Animal.num_of_animal += 1

class Dog(Animal): 
    def __init__(self):
        super().__init__()


class Cat(Animal):
    def __init__(self):
        super().__init__()


class Pet(Dog, Cat):
    @classmethod
    def access_num_of_animal(cls):
        return f'동물의 수는 {cls.num_of_animal}'


dog = Dog()
print(Pet.access_num_of_animal())
cat = Cat()
print(Pet.access_num_of_animal())




