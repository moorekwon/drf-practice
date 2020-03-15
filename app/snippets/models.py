from django.conf import settings
from django.db import models

# Create your models here.
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        # 쿼리셋을 불러올 때 설정
        ordering = ['created']

        # DB에서 index 설정 (Model.Meta)
        # ForeignKey/ManyToMany/OneToOne 경우, 자동 지정해 주기 때문에 필요 없음
        indexes = [
            models.Index(fields=['created'])
        ]
