from django.db import models
from django.contrib.auth.hashers import check_password, make_password
# Create your models here.
from .utils.exceptions import EmptyPassword


class Phone (models.Model):
    phone = models.CharField(primary_key=True,max_length=254,db_index=True)
    user_id = models.IntegerField(null=True)
    balance = models.FloatField(default=0)
    password = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)            #用来表示此手机手否还在使用

    def is_authenticate(self):
        return True

    def check_user_password(self, password):
        return check_password(password, self.password)

    @staticmethod
    def create_phone(phone, password):
        if password == '':
            raise EmptyPassword

        encode_password = make_password(password)
        return Phone.objects.create(phone=phone, password=encode_password)

    def __str__(self):
        return self.phone




