from rest_framework.views import APIView
from likemedia.models import LikeMedia
from account.models import UserProfile
from likemedia.serializers.likes import LikeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics
from usermedia.models import UserMedia

class LikeCreateView(APIView):
    '''
        Like image.
        ____________________
    '''
    permission_classes = (IsAuthenticated,)
    def get(self, request, image_id):
        liker = request.user.userprofile
        media = UserMedia.objects.get(pk=image_id)
        try: 
            like = LikeMedia.objects.get(user=liker, media=media)
            like.delete()
            
            #return Response({'message':'You have already liked this user'})
        except:
            like = LikeMedia()
            like.user = liker
            like.media = media
            like.save()
            
        return Response(LikeSerializer(like).data)