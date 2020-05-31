from rest_framework.response import Response
from collections import OrderedDict
from rest_framework import pagination

class CustomPagination(pagination.LimitOffsetPagination):

    def get_paginated_response(self, data):

        obj_list = []
        ids_list = []
        for i in data:
            ids_list.append(i['id'])  
            obj_list.append(i)          
        return Response(OrderedDict([
            ('totalCount', self.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('payload', obj_list),
            ('ids', ids_list),
            ('status', 0)
        ]))
