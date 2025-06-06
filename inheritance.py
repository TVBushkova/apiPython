class Person():
    '''Модель человека'''
    def __init__(self, name, age, height):
        '''Инициализируем атрибуты человека'''
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100
        print('Человек создан')

    def description_person(self):
        '''Получение описания человека'''
        description = self.name + ', ему ' + str(self.age) + ', его рост ' + str(self.height) + 'см, его вес ' + str(self.weight) + 'кг'
        print(f'Нового человека зовут {description}')

    def get_weight(self):
        '''Получение веса человека'''
        print(f'Вес нашего человека {str(self.weight)} кг')

    def update_weight(self, new_weight):
        '''Изменение веса человека'''
        self.weight = new_weight


class Warrior(Person):
    '''Создаем класс воина'''

    def __init__(self, name, age, height):
        '''Инициализируем атрибуты класса родителя'''
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        '''Получение веса человека'''
        return self.rage

    def description_person(self):
        '''Переопределние метода родителя'''
        description = self.name + ', ему ' + str(self.age) + ', ' + 'его заряд ярости ' + str(self.rage)
        print(f'Нового человека зовут {description}')

warrior = Warrior('Konan', 32, 200)
warrior.description_person()
print(warrior.get_rage())
