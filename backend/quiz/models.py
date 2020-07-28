from django.db import models
from django.utils.translation import ugettext_lazy as _
import pytils
from account.models import UserProfile

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


    user = models.ForeignKey(UserProfile, verbose_name=_(u'User'), null=True, blank=True, on_delete=models.SET_NULL)
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
        #print self.answers_ru
        #print self.answers_en
        #print ans
        #import pdb; pdb.set_trace()
        for a in self.answers_ru.split(','):
            if ans == a.upper():
                return True
        for a in self.answers_en.split(','):
            if ans == a.upper():
                return True
        return False        

    def __str__(self):
        return self.question
    # def save(self, **kwargs):

    #     if len(self.question_ru)> 0 and len(self.question_en)> 0:
    #         self.lang = 'ru-en'    
    #     elif len(self.question_ru)> 0:
    #             self.lang = 'ru'
    #     elif len(self.question_en)> 0:
    #             self.lang = 'en'        


    #     return super(Question, self).save(**kwargs)