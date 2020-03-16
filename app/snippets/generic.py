from rest_framework import generics, permissions

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, SnippetCreateSerializer


class SnippetListCreateAPIView(generics.ListCreateAPIView):
    pagination_class = None
    queryset = Snippet.objects.all()
    # serializer_class = SnippetSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
    ]


    # 모델을 분리했음
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SnippetSerializer
        elif self.request.method == 'POST':
            return SnippetCreateSerializer

    # 함수의 기본 코드는 serializer.save()
    # create 할 때 author 넣어주어야 함
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class SnippetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
