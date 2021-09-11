# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class User(peewee.Model):
    id = IntegerField(primary_key=True)
    name = CharField(max_length=255)
    group = CharField(max_length=255, null=True)

    class Meta:
        table_name = "user"
