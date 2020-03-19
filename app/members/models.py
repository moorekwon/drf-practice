'''
Authentication
- DRF에는 즉시 사용할 수 있고, 통합된 인증 체계가 있음
- 하지만, 구체적인 내용이 필요한 경우 고유한 체계를 customizing 할 수 있음

SessionAuthentication
- Django가 제공하는 인증을 위해 기본 session backend를 사용
- user가 성공적으로 인증되면, User 인스턴스는 request.user에 저장됨

TokenAuthentication
- 기본 앱(native app)과 같은 클라이언트-서버 설정 시 사용 권장

OAuth 및 OAuth2
- 이전에 DRF에 통합되었지만, 해당 모듈이 이동되었고 이제 타사 패키지로 지원
'''

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# 커스텀 유저 만들기
class User(AbstractUser):
    img_profile = models.ImageField('프로필 이미지', blank=True, upload_to='userimgs/')
    name = models.CharField('이름', max_length=100)


# Create your models here.
# user들을 위한 토큰 생성
# 기존 사용자
# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)


# 새로 만든 사용자
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
