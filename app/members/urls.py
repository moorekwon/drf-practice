from django.urls import path
from rest_framework.authtoken import views

from members import apis
from members.apis import LoginAPIView
from members.views import naver_login, login_view

app_name = 'members'
urlpatterns = [
    # 토큰 얻기
    # DRF는 username과 password가 지정된 토큰을 얻기 위해 내장된 뷰를 제공
    # path('api-token-auth/', views.obtain_auth_token),

    # path('auth-token/', apis.AuthTokenAPIView.as_view(), name='auth-token'),
    path('login/', LoginAPIView.as_view(), name='login'),
    # path('login/', login_view, name='login'),
    path('naver-login/', naver_login, name='naver-login'),
]
