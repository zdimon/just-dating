from rest_framework import generics
from quiz.serializers.theme import ThemeSerializer
from quiz.models import Theme


from rest_framework import viewsets

class ThemeListView(generics.ListAPIView):
    '''
    
    Theme list.


    '''
    serializer_class = ThemeSerializer
    # filterset_class = MessageFilter
    queryset = Theme.objects.all().order_by('-id')


class ThemeListViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
