from django.urls import path

from members.views import naver_login, login_view

app_name = 'members'
urlpatterns = [
    path('login/', login_view, name='login'),
    path('naver-login/', naver_login, name='naver-login'),
]