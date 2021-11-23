from django.urls import path
from . views import *
urlpatterns = [
    path('teams/<str:pk>', TeamAPI.as_view()),
    path('bets/', BettingSystemAPI.as_view()),
    path('upcoming/add/', AddUpcomingMatchAPI.as_view()),
    path('upcoming/<int:pk>', UpcomingMatchesAPI.as_view()),
]