from django.core.management import BaseCommand
from datetime import datetime, timedelta
from BillQuery.models import Bill, Item
from Authentication.models import Phone

import random

BILL_NUM = 100
STATUS = (0, 1)
START_DATE = datetime.now()
MAX_AMOUNT = 250
MAX_DATE_SECONDS = 365 * 24 * 60 * 60
PERCENT = (0, 0.1, 0.2, 0.4, 0.6, 0.8, 1.0)


class Command(BaseCommand):
    def handle(self, *args, **options):

        ITEMS = Item.objects.all()
        PHONES = Phone.objects.all()

        for i in range(0, BILL_NUM):
            item = random.choice(ITEMS)
            phone = random.choice(PHONES)

            if item.name == u'短信':
                amount = 1
                receive = item.price
                pay = random.choice((0,1)) * item.price
            else:
                amount = random.randint(1, MAX_AMOUNT)
                receive = amount * item.price
                pay = random.choice(PERCENT) * receive

            status = 1 if pay == receive else 0
            time = START_DATE + timedelta(seconds=random.randint(0, MAX_DATE_SECONDS))

            Bill.objects.create(item=item, phone=phone,
                status=status, pay=pay, receive=receive, amount=amount, time=time
            )


