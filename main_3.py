queries = [
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
]

def quantity_search(object: list) -> dict:
    one_percent = round(100 / len(object), 2)
    word_count = {}
    for query in queries:
        count = len(query.split())
        string = f'из {count} слов'
        if string in word_count:
            word_count[string] += one_percent
        else:
            word_count[string] = one_percent
    for key, value in word_count.items():
        if int(value) - value == 0:
            word_count[key] = int(value)
    return word_count

if __name__ == '__main__':
    object = quantity_search(queries)
    for key, value in object.items():
        print(f'{key}: {value} %')

