import requests

url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQd2PBOf8cegLps-vR_9UaZi2EG_XgNlfI6qg&usqp=CAU'

res = requests.get(url)

name = "photos/photo1.jpg"

with open(name, "wb") as file:
    file.write(res.content)