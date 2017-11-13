from django.db import models

# Create your models here.
from Authentication.models import Phone


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField(default=0)
    name = models.CharField(max_length=12)


class Bill(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField() # 1 表示已冲销，pay=receive.
    pay = models.FloatField(default=0)
    receive = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    time = models.DateTimeField()
    phone = models.ForeignKey(Phone, null=False)
    item = models.ForeignKey(Item, null=False)

