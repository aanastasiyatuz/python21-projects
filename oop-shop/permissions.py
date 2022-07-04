def login_required(obj):
    if not obj.is_authenticated:
        raise Exception("Юзер не авторизирован")
