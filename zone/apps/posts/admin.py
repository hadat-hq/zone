from django.contrib import admin
from zone.apps.posts.models import (
    Forum,
    Post
)


@admin.register(Forum)
class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'community_type')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'forum', 'created_at')

    list_filter = ('post_type', 'media_type')