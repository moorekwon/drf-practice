from django.contrib import admin

# Register your models here.
from amantha.models import SendStar, SendLikes


@admin.register(SendStar)
class SendStarAdmin(admin.ModelAdmin):
    pass


@admin.register(SendLikes)
class SendLikesAdmin(admin.ModelAdmin):
    pass
