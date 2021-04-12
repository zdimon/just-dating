from rest_framework import serializers
from quiz.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Question 
        fields = (
            'lang', 
            'level', 
            'tp', 
            'mode', 
            'theme', 
            'question',  
            'answers', 
            'is_published',  
            'order'
        )