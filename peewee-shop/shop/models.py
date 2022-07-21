import peewee

from abstract.models import BaseModel
from account.models import MyUser

class Product(BaseModel):
    category = peewee.CharField(max_length=100)
    title = peewee.CharField(max_length=70)
    price = peewee.DecimalField(max_digits=10, decimal_places=2)
    description = peewee.TextField()

class Comment(BaseModel):
    user = peewee.ForeignKeyField(MyUser, related_name='comments', on_delete='cascade')
    product = peewee.ForeignKeyField(Product, related_name='comments', on_delete='cascade')
    body = peewee.TextField()
    created_at = peewee.DateTimeField()
