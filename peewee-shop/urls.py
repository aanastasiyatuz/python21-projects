from account.views import register
from shop.views import create_product, product_list, create_comment

urlpatterns = [
    ('register/', register),

    ('create-product/', create_product),
    ('product-list/', product_list),
    
    ('create-comment/id', create_comment),
]
