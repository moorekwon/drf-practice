# serializer에서 필드를 동적으로 수정
# 응답으로 제한된 수의 매개변수를 추출하기 위해 웹 API가 훨씬 쉬워짐
# 초기화 시점에 serializer가 사용해야 할 필드를 설정한다고 가정
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from members.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'username',
            'email',
        )


# class CreateUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fiels = (
#             'pk',
#             # 'username',
#             'password',
#             'email',
#         )
#
#     def create(self, validated_data):
#         user = User.objects.create_user(
#             validated_data['email'], None, validated_data['password']
#         )
#         return user


# 연결되는 모델이 없어서 Serializer 사용
class LoginUserSerializer(serializers.Serializer):
    # username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        username = User.objects.get(email=data['email']).username
        password = data['password']
        user = authenticate(username=username, password=password)

        if user:
            return user
        raise serializers.ValidationError('제공된 자격증명으로 로그인할 수 없습니다.')
