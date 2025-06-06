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
        description = self.name + ', ему ' + str(self.age) + 'лет, его рост ' + str(self.height) + 'см, его вес ' + str(self.weight) + 'кг'
        print(f'Нового человека зовут {description}')

    def get_weigth(self):
        '''Получение веса человека'''
        print(f'Вес нашего человека {str(self.weight)} кг')

    def update_weight(self, new_weight):
        '''Изменение веса человека'''
        self.weight = new_weight
        return self.weight


