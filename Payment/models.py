from django.db import models
from Authentication.models import Phone,Worker
# Create your models here.

class Channel(models.Model):
    channel_id=models.AutoField(primary_key=True)
    channel_name=models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.channel_name





class Payrecord(models.Model):
    payrecord_id = models.AutoField(primary_key=True)
    payrecord_time =models.DateTimeField(auto_now=True,null=False)
    payrecord_money = models.IntegerField(null=False)
    payrecord_way =models.CharField(max_length=12,null=False)
    channel =models.ForeignKey(Channel,null=False)
    worker=models.ForeignKey(Worker)
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.phone


