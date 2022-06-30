"============CRUD=============="
# Create - создать
# Read - прочитать
# Update - обновить
# Delete - удалить

from utils import validate_id, read_db, write_to_db


database = read_db("db.json")


def read(u_id, update=False):
    """
    Принимает id юзера
    Выводит его имя и информацию
    Если такого юзера нет вызывается Exception
    """
    validate_id(database.keys(), u_id)
    name = database[u_id]["name"]
    info = database[u_id]["info"]
    sex = database[u_id]["sex"]
    if update:
        print(f"""
    ===========Update user: {u_id}============
    Name: {name}
    Sex: {sex}
    Info: {info}
    ==========================
    """)
    else:
        print(f"""
    ==========={u_id}============
    Name: {name}
    Sex: {sex}
    Info: {info}
    ==========================
    """)



def create():
    """
    Запрашивает данные о пользователе
    Записывает в бд
    """
    from utils import generate_id, validate_passwords
    name = input("Введите имя: ")
    password = input("Введите пароль: ")
    password2 = input("Введите подтверждение пароля: ")
    validate_passwords(password, password2)
    info = input("Введите информацию о вас: ")
    sex = input("Укажите пол (м,ж): ")
    id_ = generate_id(database.keys())
    database[id_] = {
        "name": name,
        "password": password,
        "info": info,
        "sex": sex
    }
    print("Вы были успешно добавлены в Python21")
    write_to_db("db.json", database)
    return id_


def delete(u_id):
    """
    Принимает id пользователя
    Если юзер существует, он удаляется из базы данных
    Если юзера нет, вызывается ошибка
    """
    validate_id(database.keys(), u_id)
    name = database[u_id]["name"]
    sex = database[u_id]['sex']
    del database[u_id]
    if sex == 'м':
        print(f"{name} был успешно удален")
    else:
        print(f"{name} была успешно удалена")
    write_to_db("db.json", database)

def update(u_id):
    """
    Принимает id юзера
    Выводит старые данные
    Принимает новые данные
    Изменяет в базе данных
    """
    validate_id(database.keys(), u_id)
    read(u_id, update=True)
    # принимаем новые данные
    info = input("Введите информацию о вас: ")
    # изменяем в бд
    database[u_id]["info"] = info
    write_to_db("db.json", database)

