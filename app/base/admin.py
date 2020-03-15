from django.contrib import admin

# Register your models here.
from base.models import Post, Comment
from base.serializers import PostSerializer


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass