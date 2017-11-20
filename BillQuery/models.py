from django.db import models

# Create your models here.
from Authentication.models import Phone


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.FloatField(default=0)
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name


UNPAID = 0 # 1 表示已冲销
PAID = 1 # 0表示未交清


class Bill(models.Model):

    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=UNPAID)
    pay = models.FloatField(default=0)#已交金额
    receive = models.FloatField(default=0)#应收金额
    amount = models.FloatField(default=0)#数量
    time = models.DateTimeField()#时间
    phone = models.ForeignKey(Phone, null=False)
    item = models.ForeignKey(Item, null=False)

    @staticmethod
    def create_bill(phone_number, item_name, amount, time):
        phone_account = Phone.objects.get(phone=phone_number)
        item = Item.objects.get(name=item_name)
        receive = item.price * amount
        return Bill.objects.create(
            phone=phone_account, amount=amount, time=time, receive=receive, item=item
        )


