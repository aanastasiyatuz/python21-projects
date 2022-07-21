from .models import MyUser

def register():
    username = input("Введите username: ")
    password = input("Введите пароль: ")
    MyUser.create(username=username, password=password)
    return "Юзер успешно зареган"
