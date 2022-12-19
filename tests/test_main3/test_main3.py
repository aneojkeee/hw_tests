import pytest
from main_3 import quantity_search

queries = [[
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сводить детей в новый зоопарк',
    'пригласить мою жену на свидание',
    'где мне можно поспать',
    'заявление на'
],
    [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'заявление на',
        'курс по питону'
    ]]


@pytest.mark.parametrize('queries', queries)
def test_len(queries):
    result = quantity_search(queries)
    assert len(result) > 0, f'Длина {len(result)} не правильная!'


@pytest.mark.parametrize('queries', queries)
def test_on_dict(queries):
    result = quantity_search(queries)
    assert type(result) == dict, 'Полученный результат не является словарем!'
    assert type(result) not in (int, float, tuple, list, set, str, bool)


@pytest.mark.parametrize('queries', queries)
def test_is_instance(queries):
    result = quantity_search(queries)
    for element in result.values():
        assert isinstance(element, int), f'Значения {element} не являются "int"!'


if __name__ == '__main__':
    pytest.main()



