from django.urls import path

from base.views import PostList

app_name = 'base'
urlpatterns = [
    path('post/', PostList.as_view()),
]
