from django.urls import path

from snippets import views, apis, generic

app_name = 'snippets'
urlpatterns = [
    # views.py
    # path('', views.snippet_list),
    # path('<int:pk>/', views.snippet_detail),

    # apis.py (class-based view)
    # path('', apis.SnippetListCreateAPIViwe.as_view()),
    # path('<int:pk>/', apis.SnippetRetrieveUpdateDestroyAPIView.as_view()),
    
    # generic.py
    path('', generic.SnippetListCreateAPIView.as_view()),
    path('<int:pk>/', generic.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]
