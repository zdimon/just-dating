# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from quiz.models import Question, RoomQuestion, RoomMessage, Room

import os
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Start quiz')
        Room.objects.all().delete()
        RoomQuestion.objects.all().delete()
        room = Room()
        room.save()
        cnt = 0
        for q in Question.objects.all().order_by('?'):
            q2r = RoomQuestion()
            q2r.question = q
            q2r.room = room
            q2r.save()
            print('Creating ... %s' % q)
            if cnt == 0:
                room.current_question = q
                room.save()
                cnt =+ 1
        