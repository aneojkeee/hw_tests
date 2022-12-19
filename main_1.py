geo_logs = [
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
]


def filter_on_list(object: list) -> list:
    filter = []
    for element in object:
        for country in element.values():
            if 'Россия' in country:
                filter.append(element)
    return filter

if __name__ == '__main__':

    for element in filter_on_list(geo_logs):
        print(element)
