import os


def dir():
    while True:
        way = input('Введите директорию:')
        if os.path.isdir(way):
            return way
        else:
            print('Вы ввели неправильный путь к файлу')


def dict_way_size(way):
    print('...Загрузка...')
    dict1 = {}
    for root, dirs, files in os.walk(way):
        for file in files:
            newkey = {os.path.join(root, file): os.path.getsize(root + '\\' + file)}
            dict1.update(newkey)
    return dict1


def analysis(dict1):
    duplicate = {}
    for key1 in dict1:
        for key2 in dict1:
            if key1[key1.rfind('\\'):] == key2[key2.rfind('\\'):] and dict1[key1] == dict1[key2] and key1 != key2:
                if key1 not in duplicate:
                    duplicate.update({key1: dict1[key1]})
    return duplicate


def duplicate(duplicate):
    if duplicate == {}:
        print('Нет дубликатов')
    list_print = []
    for key1 in duplicate:
        if key1 not in list_print:
            print()
            print(f'({duplicate[key1]}, {key1})')
            for key2 in duplicate:
                if key1[key1.rfind('\\'):] == key2[key2.rfind('\\'):] and duplicate[key1] == duplicate[key2] and not \
                        key1 == key2:
                    print(key2)
                    list_print.append(key2)


if __name__ == '__main__':
    duplicate(analysis(dict_way_size(dir())))
