ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def ids_filter(object: dict) -> list:

    object_set = set()
    for value in object.values():
        for item in value:
            object_set.add(item)
    return list(object_set)


if __name__ == '__main__':
    my_list = ids_filter(ids)
    print(my_list)