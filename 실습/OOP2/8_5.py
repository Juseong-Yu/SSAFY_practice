class Dog():
    sound = '멍멍'

class Cat():
    sound = '야옹'

class Pet(Dog, Cat):
    def __str__(self):
        return f'애완동물은 {super().sound} 소리를 냅니다.'
    
pet1 = Pet()
print(pet1)

class Dog():
    sound = '멍멍'

class Cat():
    sound = '야옹'

class Pet(Cat, Dog):
    def __str__(self):
        return f'애완동물은 {super().sound} 소리를 냅니다.'
    
pet1 = Pet()
print(pet1)