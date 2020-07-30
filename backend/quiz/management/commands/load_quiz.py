# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from quiz.models import Theme, Question
from backend.settings import FIXTURES_PATH
import os
import json

class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(FIXTURES_PATH, "questions")
        print(path)
        files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        for f in files:
            with open(os.path.join(path, f)) as j_file:
                js = json.loads(j_file.read())
                print("Current category: %s" % js['category'])
                t = Theme()
                t.name = js['category']
                t.save()
                for q in js['questions']:
                    question = Question()
                    question.theme = t
                    question.question = q['question']
                    #q['answer'] = q['answer'].replace(u'Другое','').strip()
                    ans = q['answer'].upper()
                    ans = ans.replace('"','')
                    ans = ans.replace("'",'')
                    ans = ans.replace(u"«",'')
                    ans = ans.replace(u"»",'')
                    try:
                        if len(ans.split(' '))==1 and len(ans.split('.'))==1:
                            question.answers = ans
                            try:
                                question.save()
                            except Exception as e:
                                print(str(e))
                    except:
                        pass