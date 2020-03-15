from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


# ModelSerializer - create(), update() 메소드 기본 구현
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
