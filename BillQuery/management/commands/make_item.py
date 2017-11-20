from django.core.management import BaseCommand
from BillQuery.models import Item
from io import StringIO
from django.db.utils import IntegrityError


class Command(BaseCommand):
    def handle(self, *args, **options):
        src = __file__.rsplit('.')[0] + '.txt'
        with open(src, 'rb') as f:
            content = f.read().decode(encoding='utf-8')
        f = StringIO(content)
        try:
            for line in f:
                name, p = line.strip().split()
                price = float(p)
                Item.objects.create(name=name, price=price)
        except IntegrityError:
            print('This command should be executed only once.')
        f.close()


