from django.core.management import BaseCommand
from datetime import datetime, timedelta
from BillQuery.models import Bill, Item
from Authentication.models import Phone

import random

BILL_NUM = 10
STATUS = (0, 1)
START_DATE = datetime.now()
MAX_AMOUNT = 250
MAX_DATE_SECONDS = 365 * 24 * 60 * 60


class Command(BaseCommand):
    def handle(self, *args, **options):

        ITEMS = Item.objects.all()
        PHONES = Phone.objects.all()

        for i in range(0, BILL_NUM):
            item = random.choice(ITEMS)
            phone = random.choice(PHONES)

            amount = 1 if item.name == u'短信' else random.randint(1, MAX_AMOUNT)
            receive = amount * item.price
            status = random.choice(STATUS)
            pay = receive if status == 1 else random.random() * receive

            time = START_DATE + timedelta(seconds=random.randint(0, MAX_DATE_SECONDS))

            Bill.objects.create(item=item, phone=phone,
                status=status, pay=pay, receive=receive, amount=amount, time=time
            )


