from django.urls import path
from .views import teamView, teamDetail, memberDetail
urlpatterns = [
    path('<str:pk>/', teamDetail, name='team_detail'),
    path('', teamView, name='team_view'),
    path('member/<str:pk>/info', memberDetail, name='member_detail'),
]