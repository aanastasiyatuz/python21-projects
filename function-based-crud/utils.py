"""Файл с дополнительными функциями"""


def generate_id(ids):
    """
    Принимает список существующих id
    Возвращает новое id в диапазоне от 100 до 1000
    """
    import random
    id_ = random.randint(100, 1000)
    while id_ in ids:
        id_ = random.randint(100, 1000)
    return str(id_)

def validate_passwords(p1, p2):
    """
    Принимает 2 пароля
    Если они не совпадают, вызывается ошибка
    """
    if p1 != p2:
        raise Exception("Пароли не совпадают")

def validate_id(ids, u_id):
    """
    Принимает список существующих id и id, которое нужно проверить
    Если такого id нет в списке, вызывается Exception
    """
    if u_id not in ids:
        raise Exception("Такого юзера нет")


def read_db(name):
    """
    Принимает название файла
    Возвращает данные из бд в виде python обьектов
    """
    import json
    with open(name, "r") as file:
        db = json.load(file)
    return db

def write_to_db(name, data):
    """
    Принимает название файла и данные для записи
    Записывает эти данные в файл
    """
    import json
    with open(name, "w", encoding='utf8') as file:
        json.dump(data, file, ensure_ascii=False)
