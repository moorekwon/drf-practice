from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
from config import settings

# user들이 평가한 별점
User = get_user_model()


class SendStar(models.Model):
    STAR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    star = models.CharField(choices=STAR, max_length=6)
    # 최종평점, 상위, 심사진행률?, 나에게 높은 점수를 준 이성, 등 메소드 추가하여 알고리즘 짜기


# 호감 표시
class SendLikes(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like = models.BooleanField()
