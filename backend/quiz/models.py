from django.db import models
from django.utils.translation import ugettext_lazy as _
import pytils
from account.models import UserProfile
from django.contrib.postgres.fields import JSONField
<<<<<<< HEAD
import random 
import uuid 
=======
import hashlib
import time
import uuid 
from backend.celery import app
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token
>>>>>>> b668b8c072aa290a558879c31c8f966f1ad550ab

class Theme(models.Model):
    """
    Темы вопросов.
    """
    slug = models.SlugField(help_text=_(u"Alias"))
    name = models.CharField(help_text=_(u"Name"), max_length=100)
    def __unicode__(self):
        return self.name
    def save(self, **kwargs):
        if not self.id:
            self.slug = pytils.translit.slugify(self.name)
        return super(Theme, self).save(**kwargs)

class Question(models.Model):
    '''
        Questions
    '''
    level = (
        ('1', _('Elementary')),
        ('2', _('Easy')),
        ('3', _('Middle')),
        ('4', _('Hard')),
        ('5', _('Very hard'))
    )
    lang = (
        ('ru', _('Russian')),
        ('en', _('English')),
        ('ru-en', _('Russian and English')),
      
    )
    tp =  (
        ('fullmatch', _('Full match')),
        ('substring', _('Substring match'))
    )


    lang = models.CharField(help_text=_(u"Language"), max_length=5, default="ru")
    level = models.IntegerField(help_text=_(u"Level"), default="3")
    tp = models.CharField(help_text=_(u"Mode of quize"), max_length=12, default="questionend")
    mode = models.CharField(help_text=_(u"Type of matching"), max_length=10, default="fullmatch")
    theme = models.ForeignKey(Theme, null=True, blank=True, on_delete=models.SET_NULL)
    question = models.TextField(verbose_name=_(u"Question"))
    answers = models.TextField(verbose_name=_(u"Answers"), default='', help_text=_('Divided by coma')) 
    is_published = models.BooleanField(default=True)
    order = models.IntegerField(help_text=_(u"Order"), default="1")

    @property
    def is_edit(self):
        return False

    def get_answers(self):
        return self.answers
        
    def check_answer(self,ans):
        ans = ans.upper()
        for a in self.answers_ru.split(','):
            if ans == a.upper():
                return True
        for a in self.answers_en.split(','):
            if ans == a.upper():
                return True
        return False        

    def __str__(self):
        return self.question




ROOM_TYPES = (
        ('questionend', _('Till questions are fineshed.')),
        ('infinite', _('Infinite quize (looping over questions).')),
        ('custom', _('Custom. Defining question by author.'))
    )

class Room(models.Model):
    '''
        Викторины, которые активны в настоящее время. 
        Используются для переодического опроса и перехода на новый вопрос, 
        если вышло время ответа. 
        Так же для завершения викторины по времени или по окончанию очереди вопросов.
    '''
   


    type = models.CharField(verbose_name=_(u'Quiz type'), max_length=50, choices=ROOM_TYPES, default='infinite')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_(u'Created at'))
    current_question = models.ForeignKey(Question, verbose_name=_(u'Cur question'), null=True, blank=True, on_delete=models.SET_NULL)
    is_done = models.BooleanField(default=False)
    token = models.CharField(help_text=_(u"Token"), max_length=100, db_index=True)

<<<<<<< HEAD
    def __unicode__(self):
        return self.quiz.name

    def get_absolute_url(self):
       return reverse("quiz:room_detail", kwargs={"token": self.token})

    # def get_users(self):
    #     out = ''
    #     for u in RoomUsers.objects.filter(room=self):
    #         out = out + u.user.username
    #     return out

    # def get_cnt_questions(self):
    #     return self.roomquestion_set.count()

    # def get_cnt_users(self):
    #     return RoomUsers.objects.filter(room=self).count()

    # def get_current_question_number(self):
    #     return self.current_question+1

    
    # def get_current_question_obj(self):
    #     return Question.objects.get(pk=self.questions_json[self.current_question])    

    # def save(self, **kwargs):
    #     if not self.id:
    #         self.token = hashlib.md5("%s" % int(time.time())).hexdigest()
    #     return super(Room, self).save(**kwargs)

    # def mix_question(self):
    #     '''
    #        Reranges randomly the questions in the questions_json
    #     '''    
    #     lst = []
    #     for q in self.roomquestion_set.all().order_by('?'):
    #         lst.append(q.question.id)
    #     self.questions_json = lst
    #     first = Question.objects.get(pk=lst[0])
    #     self.answers = first.answers
    #     self.current_question_text = first.question
    #     self.save()


    def set_question(self, lang, level, tp, mode, theme):
        self.current_question = random.choice(Question.objects.filter(lang=lang, level=level, tp=tp, mode=mode, theme=theme), 1)


    @staticmethod
    def get_or_create(self, type, question_time, lang, level, tp, mode, theme):
        try:
            room = Room.objects.get(token = token)
        except:
            quiz = Quiz()
            quiz.questions = Question.objects.filter(lang=lang, level=level, tp=tp, mode=mode, theme=theme)
            quiz.name='First Quiz'
            quiz.slug=None
            quiz.save()

            room = Room()
            room.type = type
            room.question_time = question_time
            room.token = uuid.uuid1()
            room.current_question = random.choice(quiz.questions, 1)
            room.current_question_text = current_question.question
            room.winner = None
            room.is_done = False
            #room.questions_json = {}
            room.save()

            r2q = RoomQuestion()
            r2q.room = room
            r2q.question = room.current_question.question
            r2q.is_done = False
        
        return room
    
    
    # def next_question(self):
    #     '''
    #         Changing the current question.
    #     '''
    #     from quiz.utils import finish_quiz
    #     indx = self.current_question+1
    #     #import pdb; pdb.eset_trace()
    #     if indx == self.get_cnt_questions():
    #         finish_quiz(self)
    #     else:
    #         newq = Question.objects.get(pk=self.questions_json[indx])
    #         self.current_question_text = newq.question
    #         self.current_question = indx
    #         self.answers = newq.answers
    #         self.save()

    # def add_user(self, user):
    #     '''
    #         Добавление пользователя
    #     '''
    #     return self.user_set

    # def del_user(self, user):
    #     '''
    #         Удаление пользователя
    #     '''
    #     return self.user_set

    # def close_quiz(self):
    #     '''
    #         Закрытие викторины
    #     '''
    #     return {}
=======
    def __str__(self):
        return self.token
 
    def save(self, **kwargs):
        if not self.id:
            self.token = 'current-room'
        return super(Room, self).save(**kwargs)
>>>>>>> b668b8c072aa290a558879c31c8f966f1ad550ab


class RoomQuestion(models.Model):
    '''
        Вопросы комнаты
    '''
    question = models.ForeignKey(Question, verbose_name=_(u'Question'), on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)
    room = models.ForeignKey(Room, verbose_name=_(u'Room'), on_delete=models.CASCADE)


class RoomMessage(models.Model):
    '''
        Сообщения комнаты
    '''
    is_right = models.BooleanField(default=False)
    is_service = models.BooleanField(default=False)
    room = models.ForeignKey(Room, verbose_name=_(u'Room'), on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_(u'Text'))
    user = models.ForeignKey(UserProfile, verbose_name=_(u'User'), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def check_answer(self):
        pass

    def save(self, *args, **kwargs):
        if not self.pk:
           self.token = self.room.token
        super(RoomMessage, self).save(*args, **kwargs)
        self.send_quiz_message(self.pk)

    @app.task
    def send_quiz_message(id):
        obj = RoomMessage.objects.get(pk=id)
        print('Sending message %s' % id)
        cent_client = CentClient()
        from quiz.serializers.message import QuizRoomMessageSerializer
        from online.models import SocketConnection
        for connection in SocketConnection.objects.all():
            pass
            token, created = Token.objects.get_or_create(user=connection.user)
            payload =  { \
                        'type': 'quiz_message', \
                        'message': QuizRoomMessageSerializer(obj).data \
                       }        
            cent_client.send(token.key, payload)