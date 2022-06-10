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
            newkey = {os.path.join(root, file): os.path.getsize(os.path.join(root, file))}
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
                if os.path.basename(key1) == os.path.basename(key2) and dict1[key1] == dict1[key2] and key1 != key2:
                    result[f'({dict1[key1]}, {key1})'].append(key2)
                    trash.append(key2)
            if len(result[f'({dict1[key1]}, {key1})']) == 0:
                del result[f'({dict1[key1]}, {key1})']
            else:
                yield f'({dict1[key1]}, {key1})', result[f'({dict1[key1]}, {key1})']


def duplicate(result):
    for i in result:
        for j in i:
            if isinstance(j, list):
                for k in j:
                    print(k)
            else: print(j)
        print()


if __name__ == '__main__':
    duplicate(analysis(dict_way_size(dir())))
