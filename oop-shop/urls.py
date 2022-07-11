from shop.views import *
from account.views import *

urlpatterns = [
    ('products/', product_list),
    ('product-create/', product_create),
    ('product-detail/id', product_detail),
    ('product-update/id', product_update),
    ('product-delete/id', product_delete),
    
    ('category-create/', category_create),
    ('comment-create/', create_comment),
]
