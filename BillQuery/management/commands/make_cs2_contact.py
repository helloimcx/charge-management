# python ./manage.py make_cs2_contact
from django.core.management.base import BaseCommand
from Authentication.models import Phone, Customer
from io import StringIO
from django.db.utils import IntegrityError
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        src = __file__.rsplit('.')[0] + '.txt'
        with open(src, 'rb') as f:
            content = f.read().decode(encoding='utf-8')
        f = StringIO(content)
        try:
            for line in f:
                customer_id, customer_name, phone, gender = line.strip().split()
                balance = round(random.uniform(0, 200), 2)
                customer = Customer.objects.create(customer_id=customer_id, customer_name=customer_name, customer_gender=gender)
                Phone.create_phone(phone=phone, customer=customer, balance=balance, password='12345')
        except IntegrityError:
            print('This command should be executed only once.')
        f.close()





