from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from usermedia.serializers.image import UserImageSerializer
from usermedia.models import UserMedia
from rest_framework.parsers import MultiPartParser, DjangoMultiPartParser, JSONParser

class AddImageView(generics.CreateAPIView):
    '''
        Creating a new image.

        ____________________
    '''
    queryset = UserMedia.objects.all()
    serializer_class = UserImageSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.userprofile)

