from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

from account.serializers.init import InitSerializer
from backend.serializers.noauth import NoAuthSerializer

class InitView(APIView):
    '''
    
    Initialization request.

    Runs after initialisation of the Angular app (APP_INITIALIZER) or F5.

    Returns data about authorized user. 


    '''

    permission_classes = (IsAuthenticated,)
    @swagger_auto_schema( 
        responses={200: InitSerializer, 401: NoAuthSerializer} )
    def get(self, request, format=None):
        token, created = Token.objects.get_or_create(user=request.user)
        data = {
            'token': token.key,
            'user': request.user.userprofile
        }
        return Response(InitSerializer(data).data)