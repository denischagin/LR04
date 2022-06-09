import os


def dir():
    while True:
        way = input('Введите директорию:')
        if os.path.isdir(way):
            print('start')
            return way
        else:
            print('Вы ввели неправильный путь к файлу')


def dict_way_size(way):
    dict1 = {}
    for root, dirs, files in os.walk(way):
        for file in files:
            newkey = {os.path.join(root, file): os.path.getsize(root + '\\' + file)}
            dict1.update(newkey)
    print('Получение файлов завершено, найдено ', len(dict1))
    return dict1


def analysis(dict1):
    result = {}
    trash = []
    print('Поиск дубликатов')
    for key1 in dict1:
        if key1 not in trash:
            result[f'({dict1[key1]}, {key1})'] = []
            for key2 in dict1:
                if key1[key1.rfind('\\'):] == key2[key2.rfind('\\'):] and dict1[key1] == dict1[key2] and key1 != key2:
                    result[f'({dict1[key1]}, {key1})'].append(key2)
                    trash.append(key2)
            if len(result[f'({dict1[key1]}, {key1})']) == 0:
                del result[f'({dict1[key1]}, {key1})']
    return result


def duplicate(result):
    for key in result:
        print(key)
        for el in result[key]:
            print(el)
        print()


if __name__ == '__main__':
    duplicate(analysis(dict_way_size(dir())))
