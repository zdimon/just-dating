
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from account.serializers.user_request import UserRequesterializer


class RegistrationView(APIView):
    '''

    User registration.

    __________________

    '''

    permission_classes = (AllowAny,)
    @swagger_auto_schema( 
        request_body = UserRequesterializer, \
        responses={200: UserRequesterializer} \
        )
    def post(self, request, format=None):
        obj = UserRequesterializer(data=request.data)
        obj.is_valid(raise_exception=True)
        profile = obj.save()
        return Response({'message': 'User %s has been created' % profile.username})