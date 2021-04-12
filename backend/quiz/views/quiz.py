from rest_framework import generics
from quiz.serializers.quiz import QuizSerializer
from quiz.models import Quiz

from rest_framework import viewsets

class QuizListView(generics.ListAPIView):
    '''
    
    Quiz list.


    '''
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all().order_by('-id')

# class QuizListViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = QuizSerializer
#     queryset = Quiz.objects.all()
