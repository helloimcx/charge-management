from Authentication.decorators import required_login
from Authentication.assist import PHONE

from .models import Bill
from .process_datatable import page_query

columns = (
    'id',
    'item__name',
    'amount',
    'pay',
    'receive',
    'time',
    'status',
)


@required_login
def data_source(request):
    phone_account = request.session[PHONE]
    assert phone_account is not None
    bills = Bill.objects.filter(phone__phone=phone_account)
    return page_query(request, bills, *columns)






