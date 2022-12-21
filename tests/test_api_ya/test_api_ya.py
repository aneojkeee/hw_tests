import requests
import pytest
import time
from api_ya import DownloaderYandex


object = DownloaderYandex('token_yandex')
name_folders = list(time.gmtime()[0:3])[::-1]
name_folders = '.'.join(list(map(str, name_folders))) + '_n'

@pytest.mark.parametrize('queries', [name_folders + '-000', name_folders + '-001'])
def test_delete_folder(queries):
    with pytest.raises(AssertionError):
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        responder = requests.delete(url, headers=object.headers_yandex, params={'path': queries})
        assert '<Response [204]>' in str(responder)

@pytest.mark.parametrize('queries', ['n_0', 'n_1'])
def test_create_folder(queries):
    result = object.create_folder(queries)
    assert '<Response [201]>' in str(result[1]), f'Папка не существует: {result[1]}'
    assert type(result[0]) == str, f'Имя папки не строка: {type(result[0])}'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    responder = requests.get(url, headers=object.headers_yandex, params={'path': result[0]}).json()
    assert 'disk' in responder['path'], f'Папка существует: {responder["path"]}'

@pytest.mark.parametrize('queries', ['n_0', 'n_1'])
def test_checking_folders(queries):
    result = object.create_folder(queries)
    assert '<Response [409]>' in str(result[1]), f'Папка существует: {result[1]}'


if __name__ == '__main__':
    pytest.main()
