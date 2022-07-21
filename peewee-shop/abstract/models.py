from peewee import Model
from config.db import postgres_db

class BaseModel(Model):
    class Meta:
        database = postgres_db
