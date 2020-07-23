# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import gettext as __
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import json
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from quiz.models.models import *
from .serializers import *
from .utils import CsrfExemptSessionAuthentication
from quiz.utils import update_question_signal, amdin_message_signal, check_answer
from multiprocessing import Pool
import brukva
import time
import threading
from django.middleware.csrf import get_token
from quiz.translation import I18N_interface

bclient = brukva.Client()
bclient.connect()

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def room_info(request,token):
    #import pdb; pdb.set_trace()
    room = Room.objects.get(token=token)
    
    messages = []
    for m in room.roommessage_set.all().order_by('id'):
        messages.append(serialize_message(m))

    users = []
    for u in room.roomusers_set.all():
        users.append(serialize_user(u.user,u.score))
    question = room.get_current_question_obj()
    return Response({
                        'status': 0, 
                        'token': get_token(request),
                        'question_text_ru': question.question_ru,
                        'question_text_en': question.question_en,
                        'question_lang': question.lang,
                        'messages': messages, 
                        'users': users, 
                        'name': room.quiz.name,
                        'cnt_questions': room.get_cnt_questions(),
                        'current_question_number': room.get_current_question_number(),
                        'is_done': room.is_done
                    })


@api_view(['GET'])
def join_to_room(request,token):
    user = request.user
    room = Room.objects.get(token=token)
    try:
        u2r = RoomUsers.objects.get(room=room,user=user)
    except:
        u2r =  RoomUsers()
        u2r.user = user
        u2r.room = room
        u2r.save()
    
    return Response(
        { "status": 0 }
    )

@api_view(['POST'])
@authentication_classes([CsrfExemptSessionAuthentication])
def save_message(request):
    input_data = json.loads(request.body)
    room = Room.objects.get(token=input_data['room_token'])
    question = Question.objects.get(pk=room.questions_json[room.current_question])
    m = RoomMessage()
    m.user = request.user
    m.room = room
    m.text = input_data['message']
    m.question = question
    ans = input_data['message'].upper()
    #import pdb; pdb.set_trace()
    m.is_right = check_answer(ans,room,request.user)

    m.save()
    for u in room.roomusers_set.all():
        mess = {"action": "add_message", "data": serialize_message(m)}
        #import pdb; pdb.set_trace()
        bclient.publish('channel_%s' % u.user.id, json.dumps(mess)) 

    return Response(
        { "status": 0, 'is_true':  m.is_right }
    )

@api_view(['GET'])
@permission_classes([])
def get_question(request,token):    
    '''
        получение текущего вопроса
    '''
    room = Room.objects.get(token=token)
    question = room.get_current_question_obj()
    #room.next_question()
    return Response({
        "status": 0,
        "text_ru": question.question_ru,
        "text_en": question.question_en,
        "lang": question.lang,
        "current_question": room.get_current_question_number()
    })

@api_view(['GET'])
def get_room_users(request,token):    
    room = Room.objects.get(token=token)
    users = []
    for u in room.roomusers_set.all():
        users.append(serialize_user(u.user,u.score))
    #room.next_question()
    return Response({
        "status": 0,
        "users": users
    })

@api_view(['GET'])
def get_user_info(request,room_token,user_id):    
    room = Room.objects.get(token=room_token)
    user = User.objects.get(pk=user_id)
    return Response({
        "status": 0,
        "user": (serialize_user(user))
    })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_room_winner(request,token):    
    room = Room.objects.get(token=token)
    return Response({
        "status": 0,
        "user": (serialize_user(room.winner))
    })


@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def i18n(request):    
    from quiz.models import ROOM_TYPES
    for rt in ROOM_TYPES:
        I18N_interface[rt[0]] = rt [1]
    return Response(I18N_interface)



def swith_question_async(room):
    #print 'start'
    #import pdb; pdb.set_trace()
    time.sleep(5)
    room.next_question() 
    update_question_signal(room)
    question = room.get_current_question_obj()
    ames = {
        "question_ru": '<strong>%s</strong>' % question.question_ru,
        "question_en": '<strong>%s</strong>' % question.question_en
    }
    amdin_message_signal(room, ames, 10)
    #print 'end'

@api_view(['GET'])
def next_question(request,room_token):    
    room = Room.objects.get(token=room_token)
    user = request.user
    mes = __('I don know. Next question please.')
    m = _('I don know. Next question please.')
    m = RoomMessage()
    m.user = user
    m.room = room
    m.is_service = True
    m.text = mes
    m.question = room.get_current_question_obj()
    m.is_right = False
    m.save()
    for u in room.roomusers_set.all():
        mess = {"action": "add_message", "data": serialize_message(m)}
        bclient.publish('channel_%s' % u.user.id, json.dumps(mess))
    #pool = Pool(processes=1)              # Start a worker processes.
    #result = pool.apply_async(swith_question_async, [room])
    thr = threading.Thread(target=swith_question_async, args=(room,), kwargs={})
    thr.start() # Will run "foo"
    return Response({
        "status": 0,
        "user": (serialize_user(user))
    })

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_active_rooms(request):
    rooms = []
    for r in Room.objects.filter(is_done=False):
        rooms.append(
            {
                "token": r.token,
                "name": r.quiz.name,
                "user_count": r.get_cnt_users(),
                "questions_count": r.get_cnt_questions()
            }
        )

    return Response({
        "status": 0,
        "rooms": rooms
    })
