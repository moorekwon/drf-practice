from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


# Post 모델 예시 (분리해야 각각 customizing하기 좋음)
#   List        PostSerializer (ListSerializer 라고 쓰지 말기)
#   Retrieve    PostDetailSerializer
#   Update      PostUpdateSerializer
#   Create      PostCreateSerialzier

# ModelSerializer - create(), update() 메소드 기본 구현
# List
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'pk',
            'author',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
        )


# Create
class SnippetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = (
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created'
        )
