from shop.models import Product, Category
from shop.views import product_list, product_update

cat = Category("phones")
Category("dyson")
Category("food")
Product("iphone", 234, "...", 3, cat)
Product("lenovo", 32, "...", 5, cat)
Product("samsung", 76, "...", 10, cat)

from pprint import pprint
# pprint(product_create())
pprint(product_list())
id_ = input("Введите прдукт для обновления: ")
pprint(product_update(id_))
