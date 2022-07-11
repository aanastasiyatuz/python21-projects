from urls import urlpatterns
from pprint import pprint

while True:
    try:
        url, arg = input("Введите адрес: ").split("/")
    except ValueError:
        print("Enter a valid url")
        continue

    found = False
    for uri, view in urlpatterns:
        if uri.split("/")[0] == url:
            found = True

            try:
                if arg:
                    pprint(view(arg))
                else:
                    pprint(view())
            except Exception as e:
                print(e)

    if not found:
        print("404 Url Not Found")
