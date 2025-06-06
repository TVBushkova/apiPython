from base_person import Person

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


warrior = Warrior('Ilya', 38, 190)
warrior.description_person()