from django.urls import path, include
from quiz.views.theme import ThemeListView, ThemeListViewSet

urlpatterns = [ 
    path('theme/list',ThemeListView.as_view()),
    path('theme',ThemeListViewSet),
]