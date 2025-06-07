import requests

class TestNewLocation():
    '''Работа с новой локацией'''

    def test_create_new_location(self):
        '''Создание новой локации'''

        base_url = 'https://rahulshettyacademy.com' #Базовый URL
        key = '?key=qaclick123' #Параметр для всех запросов
        post_recourse = '/maps/api/place/add/json' #Ресурс для метода POST

        post_url = base_url + post_recourse + key
        print(post_url)

        json_for_create_new_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
                "name": "Frontline house",
                "phone_number": "(+91) 983 893 3937",
                "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
                "website": "http://google.com",
                 "language": "French-IN"
        }

        result_post = requests.post(post_url, json=json_for_create_new_location)
        print(result_post.text)
        print(f'Статус код метода POST: {result_post.status_code}')
        assert 200 == result_post.status_code
        if result_post.status_code == 200:
            print('Мы создали новую локацию')

        check_post = result_post.json()
        check_info_post = check_post.get('status')
        print(f'Статус запроса: {check_info_post}')
        assert check_info_post == 'OK'
        if check_info_post == 'OK':
            print('Статус ответа верен')

        place_id = check_post.get('place_id')
        print(f'Place_id: {place_id}')

        get_recourse = '/maps/api/place/get/json'
        get_url = f'{base_url}{get_recourse}{key}&place_id={place_id}'
        print(get_url)
        result_get = requests.get(get_url)
        print(result_get.text)

        print(f'Статус код метода GET: {result_get.status_code}')
        assert 200 == result_get.status_code
        if result_get.status_code == 200:
            print('Мы проверили созданную локацию')



new_place = TestNewLocation()
new_place.test_create_new_location()