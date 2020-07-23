# -*- coding: utf-8 -*-
from .models.models import *
import json
from quiz.views.api.serializers import *
import brukva
import random
from django.db.models.aggregates import Max
from django.utils.translation import ugettext_lazy as _
bclient = brukva.Client()
bclient.connect()




def create_test_quize():
    print 'Creating test quizes'
    q = Quiz.objects.all().delete()
    for t in Theme.objects.all():
        print 'Process...%s' % t
        q = Quiz.objects.create(name=t.name, name_ru=t.name_ru, name_en=t.name_en)
        for qw in t.question_set.all():
            print 'Adding ... %s' % qw.id
            q.questions.add(qw)


def create_test_room(quiz):
    print "Creating test room"
    try:
        r = Room.objects.get(quiz=quiz).delete()
    except:
        pass
    r = Room()
    r.quiz = quiz
    r.save()
    for q in quiz.questions.all():
        #print 'add question %s ' % q
        nq = RoomQuestion()
        nq.room = r
        nq.question = q
        nq.save()
    r.mix_question()

def update_users_in_room_signal(room):
    users = []
    for u in room.roomusers_set.all():
        users.append(serialize_user(u.user,u.score))
    mes = {'action': 'update_users', 'users': users}
    for u in room.roomusers_set.all():
        roomid = 'channel_%s' % u.user.id
        bclient.publish(roomid, json.dumps(mes))



def update_question_signal(room):
    users = []
    for u in room.roomusers_set.all():
        users.append(serialize_user(u.user,u.score))
    mes = {'action': 'update_question', 'timer': 2000}
    for u in room.roomusers_set.all():
        roomid = 'channel_%s' % u.user.id
        bclient.publish(roomid, json.dumps(mes))


def amdin_message_signal(room,msg,timer=0):
    users = []
    for u in room.roomusers_set.all():
        users.append(serialize_user(u.user,u.score))
    mes = {'action': 'admin_message', 'question_ru': msg['question_ru'] , 'question_en': msg['question_en'], 'timer': timer}
    print mes
    for u in room.roomusers_set.all():
        roomid = 'channel_%s' % u.user.id
        bclient.publish(roomid, json.dumps(mes))



def add_one_win(user,room):
    user = RoomUsers.objects.get(room=room,user=user)
    question = room.get_current_question_obj()
    user.score = user.score + 1
    user.save()
    update_users_in_room_signal(room)
    ames = {
        "question_ru": '<strong>%s</strong>' % question.question_ru,
        "question_en": '<strong>%s</strong>' % question.question_en
    }    
    #ames = _('<strong>%s gave the correct answer!</strong>') % user.user.profile.get_username()
    amdin_message_signal(room, ames)

    
    amdin_message_signal(room, ames, 3000)

def check_answer(ans,room,user):
    #is_right = bool(random.getrandbits(1))
    is_right = False
    #import pdb; pdb.set_trace()
    question = room.get_current_question_obj()
    for a in question.answers_ru.split(','):
        if ans == a.upper():
            is_right = True
    for a in question.answers_en.split(','):
        if ans == a.upper():
            is_right = True

    if is_right == True:
        room.next_question()
        add_one_win(user,room)
        update_question_signal(room)

        return True
    else:
        return False

def finish_quiz(room):
    room.is_done = True
    user = RoomUsers.objects.filter(room = room).order_by('-score')[0]
    room.winner = user.user
    room.save()
    users = []
    for u in room.roomusers_set.all():
        users.append(serialize_user(u.user,u.score))
    mes = {'action': 'end_quiz'}
    for u in room.roomusers_set.all():
        roomid = 'channel_%s' % u.user.id
        bclient.publish(roomid, json.dumps(mes))

    