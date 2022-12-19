import pytest
from unittest.case import TestCase
from main_1 import filter_on_list

my_list = [[
     {'visit1': ['Москва', 'Россия']},
     {'visit2': ['Дели', 'Индия']},
     {'visit3': ['Владимир', 'Россия']}
    ],
    [
     {'visit1': ['Гонконг', 'Китай']},
     {'visit2': ['Берлин', 'Германия']}
    ],
    [
     {'visit1': ['Москва', 'Россия']},
     {'visit2': ['Дели', 'Индия']},
     {'visit3': ['Владимир', 'Россия']},
     {'visit4': ['Лиссабон', 'Португалия']},
     {'visit5': ['Париж', 'Франция']},
     {'visit6': ['Лиссабон', 'Португалия']},
     {'visit7': ['Тула', 'Россия']},
     {'visit8': ['Тула', 'Россия']},
     {'visit9': ['Курск', 'Россия']},
     {'visit10': ['Архангельск', 'Россия']}
    ]]


@pytest.mark.parametrize('my_list', my_list)
def test_len(my_list):
    result = filter_on_list(my_list)
    assert len(result) in (0, 2, 6), f'Длина {len(result)} не правильная!'


@pytest.mark.parametrize('my_list', my_list)
def test_on_list(my_list):
    result = filter_on_list(my_list)
    assert type(result) == list, 'Полученный результат не будет являться списком!'
    assert type(result) not in (int, float, tuple, dict, set, str, bool)


@pytest.mark.parametrize('my_list', my_list)
def test_find_Russia(my_list):
    result = filter_on_list(my_list)
    for element in result:
        for values in element.values():
            assert 'Россия' in values, '"Россия" - не найдено!'


if __name__ == '__main__':
    pytest.main()