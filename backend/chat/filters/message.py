from django_filters import FilterSet, NumberFilter, CharFilter
from chat.models import ChatMessage


class MessageFilter(FilterSet):
    token = CharFilter()
    class Meta:
        model = ChatMessage
        fields = ['token']