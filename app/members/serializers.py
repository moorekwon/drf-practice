# serializer에서 필드를 동적으로 수정
# 응답으로 제한된 수의 매개변수를 추출하기 위해 웹 API가 훨씬 쉬워짐
# 초기화 시점에 serializer가 사용해야 할 필드를 설정한다고 가정
from django.contrib.auth.models import User
from rest_framework import serializers


# class DynamicFieldsModelSerializer(serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         # fields 인수를 수퍼 클래스로 전달하지 x
#         fields = kwargs.pop('fields', None)
#
#         # 수퍼 클래스를 정상적으로 인스턴스화
#         super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)
#
#         # fields 인수에 지정되지 않은 모든 필드 삭제
#         if fields is not None:
#             allowed = set(fields)
#             existing = set(self.fields.keys())
#
#             for field_name in existing - allowed:
#                 self.fields.pop(field_name)


# serialzier 클래스에서 DynamicFieldsModelSerializer 확장
# class UserSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')

# fields 안에 필드 이름 언급
# serializer에서 (모두 안받고) id, email만 받음
# UserSerializer(user, fields=('id', 'email'))
