from django.urls import path
from rest_framework.authtoken import views

from base.views import PostList

app_name = 'base'
urlpatterns = [
    # 토큰 얻기
    # DRF는 username과 password가 지정된 토큰을 얻기 위해 내장된 뷰를 제공
    path('api-token-auth/', views.obtain_auth_token),
    path('post/', PostList.as_view()),
]
