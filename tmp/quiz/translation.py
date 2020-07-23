from modeltranslation.translator import translator, TranslationOptions
from .models.models import Question, Theme, Quiz
from django.utils.translation import ugettext_lazy as _

class QuestionTranslationOptions(TranslationOptions):
    fields = ('question', 'answers')

translator.register(Question, QuestionTranslationOptions)

class ThemeTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Theme, ThemeTranslationOptions)

class QuizTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Quiz, QuizTranslationOptions)


I18N_interface =  {
        "subject": _('Quizes theme'),
        "total_questions": _('Total questions'),
        "enter_help": _('Type the answer and press Enter or "?" if you give up'),
        "next": _('Next'),
        "participants": _('Participants'),
        "exit": _('Exit'),
        "quiz_ended": _('Quiz is compleat.'),
        "current_question": _('current_question'),
        "your_name": _('Your name'),
        "menu_home": _('Home'),
        "menu_my_questions": _('My questions'),
        "menu_quiz": _('Quiz'),
        "active_rooms": _('Active rooms'),
        "name": _('Name'),
        "user_count": _('Number of users'),
        "questions_count": _('Number of questions'),
        "question": _('Question'),
        "answers": _('Answer'),
        "edit": _('Edit'),
        "delete": _('Delete'),
        "level": _('Level'),
        "no_data": _('No data'),
        "total": _('Total'),
        "current_page": _('Current page'),
        "edit": _('Edit'),
        "publish": _('Publish'),
        "filter": _('Filter'),
        "translate": _('Translate'),
        "category": _('Category'),
        "unpublish": _('Unpublish'),
        "create_question": _('Create question'),
        "save": _('Save'),
        "clear_filter": _('Clear filter'),
        "create_room": _('Create room'),
        "required": _('This is required field.'),
        "type_room": _('Type of the room'),
        "join": _('Join')
}

