from .models import Bill, Item
from Authentication.decorators import required_login


@required_login
def pager_query(request):
    draw    = request.GET['draw']
    length  = request.GET['length']
    start   = request.GET['start']
    #
    # TODO
    #
    ret = {
        'draw':draw,
        'recordsTotal':'0',
        'recordsFiltered':'0',
        'data':[],
    }

    return ret


