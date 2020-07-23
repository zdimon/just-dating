# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
import os
import json
from quiz.models.models import *
from random import randint

class Command(BaseCommand):
    def handle(self, *args, **options):
        print 'Creating math quiz'
        try:
            t = Theme.objects.get(slug='simple-math')
        except:
            print 'Create theme'
            t = Theme.objects.create(name="Simple math")

        try:
            quiz = Quiz.objects.get(slug='multiplication-table')
        except:
            print 'Create quiz'
            quiz = Quiz.objects.create(name="Multiplication table")
        print 'Clearing....'
        Question.objects.filter(theme=t).delete()
        for n in range(2,10):
            nn = randint(1, 9)
            txt = '%s * %s = ?' % (n,nn)
            ans = n*nn
            q = Question()
            q.theme = t
            q.lang = 'ru-en'
            q.question = txt
            q.answers = ans
            q.tp = 'fullmatch'
            q.save()
            quiz.questions.add(q)
            print 'Saving %s * %s' % (n,nn)
        for n in range(2,10):
            nn = randint(1, 9)
            ch = n*nn
            txt = '%s / %s = ?' % (ch,n)
            q = Question()
            q.theme = t
            q.lang = 'ru-en'
            q.question = txt
            q.answers = nn
            q.tp = 'fullmatch'
            q.save()
            quiz.questions.add(q)
            print 'Saving %s / %s = %s' % (ch,n,nn)     
        for n in range(2,20):       
            nn = randint(4, 30)
            otv = n+nn
            txt = '%s + %s = ?' % (nn,n)
            q = Question()
            q.theme = t
            q.lang = 'ru-en'
            q.question = txt
            q.answers = otv
            q.tp = 'fullmatch'
            q.save()
            quiz.questions.add(q)
            print 'Saving %s / %s = %s' % (nn,n,otv) 
        