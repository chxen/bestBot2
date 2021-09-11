from peewee import Model, IntegerField, CharField

from .database import db


class User(Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    group = CharField(null=True)

    class Meta:
        database = db
