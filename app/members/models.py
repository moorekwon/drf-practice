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

from amantha.models import SendStar


# 커스텀 유저 만들기
class User(AbstractUser):
    GENDER = (
        ('남자', '남자'),
        ('여자', '여자'),
    )

    BODY_TYPE = (
        ('슬림한', '슬림한'),
        ('뚱뚱한', '뚱뚱한'),
    )

    PERSONALITY = (
        ('착한', '착한'),
        ('엉뚱한', '엉뚱한'),
    )

    BLOOD_TYPE = (
        ('AB', 'AB'),
        ('B', 'B'),
        ('A', 'A'),
        ('O', 'O'),
    )

    DRINKING_STYLE = (
        ('안 마심', '안 마심'),
        ('가끔 마심', '가끔 마심'),
        ('많이 마심', '많이 마심'),
    )

    SELECT_STORIES = (
        ('1번', '1번'),
        ('2번', '2번'),
        ('3번', '3번'),
        ('4번', '4번'),
    )

    SELECT_TAGS = (
        ('연애 스타일', '연애 스타일'),
        ('데이트 스타일', '데이트 스타일'),
        ('나만의 매력', '나만의 매력'),
        ('라이프 스타일', '라이프 스타일'),
    )

    star_rating = models.ForeignKey(SendStar, on_delete=models.CASCADE, related_name='my_star', null=True)
    email = models.EmailField()
    gender = models.CharField(choices=GENDER, max_length=6)
    img_profile = models.ImageField('프로필 이미지', blank=True, upload_to='user_images/')
    university = models.CharField(max_length=30, blank=True)
    major = models.CharField(max_length=30, blank=True)
    job = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=30)
    birth = models.DateField(null=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    body_type = models.CharField(choices=BODY_TYPE, max_length=10)
    personality = models.CharField(choices=PERSONALITY, max_length=10)
    blood_type = models.CharField(choices=BLOOD_TYPE, max_length=6)
    smoking = models.BooleanField(null=True)
    drinking = models.CharField(choices=DRINKING_STYLE, max_length=10)
    # active = models.BooleanField()

    # 추가 프로필 - 소개글 작성
    introduction = models.TextField(max_length=150, blank=True)
    # 추가 프로필 - 스토리 작성
    select_stories = models.CharField(choices=SELECT_STORIES, max_length=60, blank=True)
    # 추가 프로필 - 관심태그 선택
    select_tags = models.CharField(choices=SELECT_TAGS, max_length=20, blank=True)



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
