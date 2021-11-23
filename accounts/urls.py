from django.urls import path
from . views import signup_view, activation_sent_view, activate, signin_view, logout_view


urlpatterns = [
    path('signin/', signin_view, name="signin"),
    path('signup/', signup_view, name="signup"),
    path('logout/', logout_view, name="logout"),
    path('sent/', activation_sent_view, name="activation_sent"),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),
]