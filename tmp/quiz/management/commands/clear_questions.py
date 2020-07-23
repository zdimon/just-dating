# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from quiz.models import Theme, Question
from dj.settings import BASE_DIR
import os
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        print ('Clearing...')
        for q in Question.objects.all():
            try:
                cnt =len(q.answers[0].split(' '))
                if(cnt>1):
                   q.delete()
                   print 'Deleting' 
                cnt =len(q.answers[0].split('.'))
                if(cnt>1):
                   q.delete()
                   print 'Deleting ....' 
            except:
                pass
            q.answers = q.answers.replace('["','').replace('"]','')
            q.save()

