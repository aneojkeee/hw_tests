import requests
import json
import time
from alive_progress import alive_bar


class Uploader:

    URL = 'https://api.vk.com/method/'

    def __init__(self, version='5.194'):

        with open('token_vk.txt') as file:
            self.token_vk = file.readline()

        self.params_vk = {
            'access_token': self.token_vk,
            'v': version}

    def get_list_albums(self, id_user=None):

        url = Uploader.URL + 'photos.getAlbums?'
        parameters = {'owner_id': id_user}
        list_albums = []

        response = requests.get(url, params={
            **self.params_vk, **parameters}).json()
        time.sleep(0.33)

        for element in response['response']['items']:
            new_dict = {}
            new_dict['id'] = element['id']
            new_dict['size'] = element['size']
            list_albums.append(new_dict)
        return list_albums

    def get_photos(self, id_user, id_album='profile', count=5):

        url = Uploader.URL + 'photos.get?'
        parameters = {
            'owner_id': id_user,
            'album_id': id_album,
            'extended': 1,
            'photo_sizes': 1,
            'count': count
        }

        list_photos = []
        response = requests.get(url, params={
            **self.params_vk, **parameters}).json()
        time.sleep(0.33)

        if 'error' in response:
            print('\nОшибка запроса Api VK: ', response['error']['error_msg'], end='\n\n')

        for element in response['response']['items']:
            new_dict = {}

            new_dict['sizes'] = element['sizes'][-1]['type']
            new_dict['url'] = element['sizes'][-1]['url']
            new_dict['likes'] = element['likes']['count']
            new_dict['album_id'] = element['album_id']

            list_photos.append(new_dict)
        return list_photos


class DownloaderYandex:

    def __init__(self, token):

        self.token_yandex = token
        self.headers_yandex = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token_yandex}'}

    def save_photos_to_yandex(self, list_photos):

        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        list_name = []

        print("Выгрузка фото в Я.Диск:")
        with alive_bar(len(list_photos), force_tty=True, dual_line=True) as bar:
            for element in list_photos:
                name_folder = self.create_folder(element['album_id'])
                name_file = self.create_name_file(element, list_name)
                name_path = name_folder + '/' + name_file
                parameters = {
                    'path': name_path,
                    'url': element['url']
                }
                bar.text = f'Идет загрузка {name_path}, подождите ...'

                response = requests.post(
                    url, headers=self.headers_yandex, params=parameters)

                del element['likes'], element['url'], element['album_id']
                element['file_name'] = name_file
                bar()
        return list_photos

    def create_name_file(self, dict_photo, list_names):

        name_file = dict_photo['url'].split('/')[-1].split('?')[0]
        index = name_file.find('.')
        name_file = name_file[index:]
        name_file = str(dict_photo['likes']) + name_file

        if name_file in list_names:
            name = name_file.split('.')
            local_time = f'_({time.time()})'
            name[0] += local_time
            name_file = '.'.join(name)

        list_names.append(name_file)
        return name_file

    def create_folder(self, id_album):

        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        name_folders = list(time.gmtime()[0:3])[::-1]
        name_folders = '.'.join(list(map(str, name_folders)))
        name_folders += '_' + str(id_album)
        parameters = {'path': name_folders}
        requests.put(url, headers=self.headers_yandex, params=parameters)
        return name_folders


def input_userid_and_token():

    id_user = input("Введите ID пользователя: ")
    if id_user == '':
        id_user = '35174055'
    token_yandex = input("Введите токен с полигона Яндекс: ")
    if token_yandex == '':
        with open('token_yandex.txt') as file:
            token_yandex = file.readline()
    return id_user, token_yandex


if __name__ == '__main__':
    id_user, token_yandex = input_userid_and_token()

    object_vk = Uploader()
    my_photos = object_vk.get_photos(id_user, count=10)

    object_yandex = DownloaderYandex(token_yandex)
    my_json = object_yandex.save_photos_to_yandex(my_photos)

    str_reader = json.dumps(my_json, ensure_ascii=False, indent=4)
    with open('list_files.json', 'w', encoding='utf-8') as f:
        f.write(str_reader)


