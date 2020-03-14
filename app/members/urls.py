from django.urls import path

from members.views import naver_login

app_name = 'members'
urlpatterns = [
    path('naver-login/', naver_login, name='naver-login'),
]