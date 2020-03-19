# serializer에서 필드를 동적으로 수정
# 응답으로 제한된 수의 매개변수를 추출하기 위해 웹 API가 훨씬 쉬워짐
# 초기화 시점에 serializer가 사용해야 할 필드를 설정한다고 가정
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
        )
