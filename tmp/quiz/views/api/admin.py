from rest_framework import viewsets
from quiz.models.models import Question, Theme
from .serializers import QuestionSerializer, serialize_question, ThemeSerializer
from rest_framework import authentication, permissions
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
import json
from django.views.decorators.csrf import csrf_exempt
from .utils import CsrfExemptSessionAuthentication

@permission_classes((AllowAny, ))
class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    pagination_class = None
    serializer_class = ThemeSerializer

@permission_classes((AllowAny, ))
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    def get_queryset(self):
        user = self.request.user
        queryset = Question.objects.all().order_by('-id')
        queryset = queryset.filter(user=user)
        #print self.request.GET['lang']
        try:
            t = Theme.objects.get(pk = self.request.GET['theme'])
            queryset = queryset.filter(theme=t)
        except:
            pass
        try:
            queryset = queryset.filter(lang=self.request.GET['lang'])
        except:
            pass
        print queryset.query
        return queryset


@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication])
@permission_classes([])
#@csrf_exempt
def save_question(request): 
    input_data = json.loads(request.body)
    t = Theme.objects.get(pk = input_data['theme_id'])
    is_new = False
    try:
        q = Question.objects.get(pk=input_data['id'])
    except:
        q = Question()
        is_new = True
    try:
        q.question_ru = input_data['question_ru']
        q.question_en = input_data['question_en']
        q.answers_ru = input_data['answers_ru']
        q.answers_en = input_data['answers_en']
        q.level = input_data['level']
        q.theme = t
        q.user = request.user
        q.save()
    except Exception as e:
        return Response({
            "status": 1,
            "message": str(e)
        })    
    return Response({
        "status": 0,
        "is_new": is_new,
        "object": serialize_question(q)
    }) 

@csrf_exempt
@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication])
@permission_classes([])
def delete_question(request): 
    input_data = json.loads(request.body)
    try:
        q = Question.objects.get(pk=input_data['id'])
        q.delete()
    except Exception as e:
        return Response({
            "status": 1,
            "message": str(e)
        })    
    return Response({
        "status": 0,
    }) 

@api_view(['GET'])
#@authentication_classes([])
#@permission_classes([])
#@csrf_exempt
def publish_question(request,id):
    try:
        q = Question.objects.get(pk=id)
        q.is_published = True
        q.save()
    except Exception as e:
        return Response({
            "status": 1,
            "message": str(e)
        })  
    return Response({
        "status": 0,
    }) 

@api_view(['GET'])
#@authentication_classes([])
#@permission_classes([])
#@csrf_exempt
def unpublish_question(request,id):
    try:
        q = Question.objects.get(pk=id)
        q.is_published = False
        q.delete()
    except Exception as e:
        return Response({
            "status": 1,
            "message": str(e)
        })  
    return Response({
        "status": 0,
    }) 