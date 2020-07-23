from rest_framework import routers, serializers, pagination
from rest_framework.response import Response
from django.core.mail import send_mail, EmailMessage
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


def _send_email(to_list, subject, message, sender='admin@example.com'):
    msg = EmailMessage(subject, message, sender, to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()



class ChoicesSerializerField(serializers.SerializerMethodField):
    """
    A read-only field that return the representation of a model field with choices.
    """

    def to_representation(self, value):
        # sample: 'get_XXXX_display'
        method_name = 'get_{field_name}_display'.format(field_name=self.field_name)
        # retrieve instance method
        method = getattr(value, method_name)
    
        # retrieve instance method
        method_id = getattr(value, self.field_name)
        # finally use instance method to return result of get_XXXX_display()
        #return method()
        return {'value': method(), 'id': method_id}        


class CustomPagination(pagination.LimitOffsetPagination):

    def get_has_prev(self):
        if self.get_offset(self.request) == 0:
            return False
        if self.get_current_page()==1:
            return False
        else:
            return True

    def get_has_next(self):
        if self.count >=  (self.get_current_page()+1)*self.get_limit(self.request):
            return True
        else:
            return False

    def get_current_page(self):
        if self.get_offset(self.request) == 0:
            return 1
        else:
            cel = self.get_offset(self.request) / self.get_limit(self.request)
            mod = self.get_offset(self.request) % self.get_limit(self.request)
            if mod > 0:
                return cel+1
            else:
                return cel

    def make_pager(self):
        out = []
        #if self.get_has_prev():
        #    out.append({"name": "prev", "limit": self.get_limit(self.request), "offset": self.get_offset(self.request)-self.get_limit(self.request)}) 

        #if self.get_has_next():
        #    out.append({"name": "next",  "limit": self.get_limit(self.request), "offset": self.get_offset(self.request)+self.get_limit(self.request)}) 
        return out


    def get_paginated_response(self, data):
        # import time; time.sleep(2)
        return Response({
           
            'limit': self.get_limit(self.request),
            'offset': self.get_offset(self.request),
            'next_link': self.get_next_link(),
            'count': self.count,
            'current': self.get_current_page(),
            'has_prev': self.get_has_prev(),
            'has_next': self.get_has_next(),
            'pager': self.make_pager(),
            'results': data
        })        