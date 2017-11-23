'''
处理 DataTable 的 AJAX 请求
'''
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from datetime import datetime


class CustomizedDateTimeFormatJSONEncoder(DjangoJSONEncoder):
    '''使用`TIME_FORMAT`的日期时间格式'''
    TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime(self.TIME_FORMAT)
        else:
            return super(CustomizedDateTimeFormatJSONEncoder, self).default(o)



def page_query(request, queryset, *columns):
    '''
    以`JSON`形式返回查询结果。
    :param request: Django 请求对象
    :param queryset: Django QuerySet 对象
    :param columns: 需要发送给 DataTable 的属性列，如忽略则发送所有属性列
    '''
    l = int(request.GET.get('length'))
    s = int(request.GET.get('start'))

    json_data = dict()

    json_data['draw'] = request.GET.get('draw')

    json_data['recordsTotal'] = queryset.count()
    json_data['recordsFiltered'] = json_data['recordsTotal']

    json_data['data'] = list(queryset.values_list(*columns)[s:s + l])

    return JsonResponse(data=json_data, encoder=CustomizedDateTimeFormatJSONEncoder)