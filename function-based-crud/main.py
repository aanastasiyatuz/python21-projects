from crud import create, read, update, delete

u1 = "718"
u2 = "987"
u3 = "134"
u4 = "770"

users = [u1,u2,u3,u4]
for u in users:
    # смотрим инфу о юзере
    read(u)

# обновляем
update(u4)

# создаем
id_ = create()

# удаляем
delete(id_)