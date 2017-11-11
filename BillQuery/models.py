from django.db import models

# Create your models here.
from Authentication.models import Phone


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    price = models.FloatField(default=0)
    item = models.CharField(max_length=12)


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    status = models.IntegerField()
    pay = models.FloatField(default=0)
    receive = models.FloatField(default=0)
    amount = models.FloatField(default=0)
    time = models.DateTimeField()
    account_id = models.ForeignKey(Phone, null=False)
    item = models.ForeignKey(Item, null=False)
