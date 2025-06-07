import requests

class TestNewJoke():
    '''Создание новой шутки'''

    def __init__(self):
        pass

    def test_create_new_randon_joke(self):
        url = 'https://api.chucknorris.io/jokes/random'
        result = requests.get(url)
        result.encoding = 'utf-8'
        check_joke = result.json()
        #check_info = check_joke.get("categories")
        #assert check_info == []
        #print('Категория верна!')
        check_info_value = check_joke.get("value")
        print(check_info_value)
        name = "Chuck"
        if name in check_info_value:
            print("Наша шутка")

    def test_create_new_joke_category(self):
        '''Создание случайно шутки по категории'''
        category = 'sport'
        url = f'https://api.chucknorris.io/jokes/random?category={category}'
        result = requests.get(url)
        result.encoding = 'utf-8'
        check_joke = result.json()
        check_info_value = check_joke.get("categories")
        print(check_info_value)
        assert check_info_value == ["sport"]
        print('Категория верна')

#random_joke = TestNewJoke()
#random_joke.test_create_new_randon_joke()

sport_joke = TestNewJoke()
sport_joke.test_create_new_joke_category()
