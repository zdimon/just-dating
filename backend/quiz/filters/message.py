from django_filters import FilterSet, NumberFilter, CharFilter
from quiz.models import RoomMessage


class RoomMessageFilter(FilterSet):
    token = CharFilter()
    class Meta:
        model = RoomMessage
        fields = ['token']