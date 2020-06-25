# author: Dmitry Zharikov zdimon77@gmail.com
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from account.serializers.login import LoginRequestSerializer, LoginResponseSerializer
from account.serializers.profile import UserProfileSerializer
from rest_framework.exceptions import AuthenticationFailed 


class LoginView(ObtainAuthToken):
    '''

    User login.

    __________________

    '''

    permission_classes = (AllowAny,)
    @swagger_auto_schema( 
        request_body = LoginRequestSerializer, \
        responses={
                    200: LoginResponseSerializer, \
        } \
        )
    def post(self, request, format=None):
        
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            profile = user.userprofile
            token, created = Token.objects.get_or_create(user=user)
            out_data = {
                'token': token,
                'user': profile
            }
            return Response(LoginResponseSerializer(out_data).data)
        else:
            raise AuthenticationFailed('Wrong username or password!')