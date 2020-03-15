from rest_framework import serializers

from snippets.models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippet


class SnippetSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField()
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    # create(data)
    def create(self, validated_data):
        return Snippet.objects.create(**validated_data)

    # update(instance, data)
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            # instance.key = value
            setattr(instance, key, value)
        instance.save()
        return instance
