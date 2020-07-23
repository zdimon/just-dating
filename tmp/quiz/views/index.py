# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from quiz.models.models import *
from rest_framework.authtoken.models import Token
from dj.settings import SOCKET_SERVER
from quiz.utils import update_users_in_room_signal
from django.shortcuts import redirect
from quiz.translation import I18N_interface
# Create your views here.


def new(request):
    '''
        Создание новой комнаты викторины.
    '''
    context = {}
    return render(request,'quiz/new.html',context)

def room_index(request):
    if(not request.user.is_authenticated()):
        request.session['try_room'] = token
        return redirect('login')
    try:
        t = Token.objects.get(user=request.user)
    except:
        t = Token.objects.create(user=request.user)
    context = {'token': t.key, 'socket_server': SOCKET_SERVER, 'i18n_interface': I18N_interface}
    print context
    return render(request,'quiz/index.html',context)

