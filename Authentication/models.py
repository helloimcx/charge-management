from django.db import models
from django.contrib.auth.hashers import check_password, make_password
from .utils.exceptions import EmptyPassword


class Customer(models.Model):
    customer_id = models.BigIntegerField(max_length=20, primary_key=True)
    customer_name = models.CharField(max_length=12, null=False)
    customer_gender = models.CharField(default="男", max_length=5, null=False)

    def __str__(self):
        return self.customer_name


class Phone (models.Model):
    account_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15, db_index=True, unique=True)
    customer = models.ForeignKey(Customer, null=False)
    balance = models.FloatField(default=0)
    password = models.CharField(max_length=255, null=False)
    is_active = models.BooleanField(default=True)            #用来表示此手机手否还在使用

    def is_authenticate(self):
        return True

    def check_user_password(self, password):
        return check_password(password, self.password)

    @staticmethod
    def create_phone(phone, customer, balance, password):
        if password == '':
            raise EmptyPassword

        encode_password = make_password(password)
        return Phone.objects.create(phone=phone, customer=customer, balance=balance,
                                    password=encode_password)

    def __str__(self):
        return self.phone


class Hall(models.Model):
    hall_id = models.AutoField(primary_key=True)
    hall_address = models.CharField(max_length=50, null=False)
    hall_name = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.hall_name


class Worker(models.Model):
    worker_id=models.AutoField(primary_key=True)
    worker_name = models.CharField(max_length=12, null=False)
    hall = models.ForeignKey(Hall, null=False)
    password = models.CharField(max_length=255, null=False)

    def is_authenticate(self):
        return True

    def __str__(self):
        return self.worker_name



