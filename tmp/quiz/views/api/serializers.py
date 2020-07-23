from rest_framework import routers, serializers, viewsets
from quiz.models.models import Question, Theme


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = (
                'id',
                'name_ru',
                'name_en'
                )


class QuestionSerializer(serializers.ModelSerializer):
    theme = serializers.StringRelatedField()
    class Meta:
        model = Question
        #is_edit = serializers.ReadOnlyField(source='is_edit')
        fields = (
                'id',
                'question_ru', 
                'question_en',
                'question',  
                'answers_ru',
                'answers_en',
                'answers',
                'level',
                'theme', 
                'lang',
                'theme_id',
                'is_published',
                'is_edit'
                )   

def serialize_question(obj):
    return {
        "id": obj.id,
        "question_ru": obj.question_ru,
        "question_en": obj.question_en,
        "answers_ru": obj.answers_ru,
        "answers_en": obj.answers_en,
        "theme": obj.theme.name,
        "theme_id": obj.theme.id,
        "lang": obj.lang,
        "level": obj.level
    }    

def serialize_user(obj,score=0):
    '''
        obj: User class
    '''
    profile = obj.profile
    return {
        "id": profile.user_id,
        "name": profile.get_username(),
        "avatar": profile.get_small_avatar_url(),
        "rating": profile.get_rating(),
        "score": score
    }


def serialize_message(obj):
    '''
        obj: RoomMessage class
    '''
    return {
        "text": obj.text,
        "is_right": obj.is_right,
        "created_at": obj.created_at.strftime("%H:%M:%S"),
        "is_service": obj.is_service,
        "user": serialize_user(obj.user)
    }