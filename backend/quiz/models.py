from django.db import models
from django.utils.translation import ugettext_lazy as _
import pytils
from account.models import UserProfile
from django.contrib.postgres.fields import JSONField
import hashlib
import time
import uuid 
from backend.celery import app
from backend.cent_client import CentClient
from rest_framework.authtoken.models import Token

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
        
    # def check_answer(self,ans):
    #     ans = ans.upper()
    #     for a in self.answers_ru.split(','):
    #         if ans == a.upper():
    #             return True
    #     for a in self.answers_en.split(','):
    #         if ans == a.upper():
    #             return True
    #     return False        

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

    def __str__(self):
        return self.token
 
    def save(self, **kwargs):
        if not self.id:
            self.token = 'current-room'
        return super(Room, self).save(**kwargs)


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
        answer = self.room.current_question.answers
        if self.text.upper() == answer:
            self.is_right = True

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
    