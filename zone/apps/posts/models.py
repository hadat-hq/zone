from django.db import models
from zone.apps.common.models import TimestampedModel

class Forum(TimestampedModel):
    PUBLIC = 'P'
    RESTRICTED = 'R'
    PRIVATE = 'PR'

    COMMUNITY_TYPES = (
        (PUBLIC, 'PUBLIC'),
        (RESTRICTED, 'RESTRICTED'),
        (PRIVATE, 'PRIVATE')
    )

    name = models.CharField(max_length=50, unique=True)
    community_type = models.CharField(max_length=3, choices=COMMUNITY_TYPES, db_index=True)
    explicit = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    @classmethod
    def get_forum_types(cls):
        return cls.COMMUNITY_TYPES
class Post(TimestampedModel):
    POST = 'P'
    MEDIA = 'M'
    URL = 'U'
    POST_TYPE_CHOICES = (
        (POST, 'POST'),
        (MEDIA, 'MEDIA'),
        (URL, 'URL')
    )

    VIDEO = 'V'
    IMAGE = 'I'

    MEDIA_TYPE_CHOICES = (
        (VIDEO, 'VIDEO'),
        (IMAGE, 'IMAGE')
    )

    post_type = models.CharField(max_length=2, choices=POST_TYPE_CHOICES, db_index=True)
    title = models.CharField(max_length=500, db_index=True)

    content = models.TextField(blank=True)
    media_url = models.CharField(max_length=500,null=True, blank=True)
    media_type = models.CharField(max_length=2, choices=MEDIA_TYPE_CHOICES, db_index=True, null=True, blank=True)
    url = models.TextField(blank=True)
    forum = models.ForeignKey(Forum, on_delete=models.SET_NULL, null=True)
    pinned = models.BooleanField(default=False)
    flag_spam = models.BooleanField(default=False)

    lock_comments = models.BooleanField(default=False)
    explicit = models.BooleanField(default=False)
    hide = models.BooleanField(default=False)
    notifications = models.BooleanField(default=True)
    def get_media_types(cls):
        return cls.MEDIA_TYPE_CHOICES
    def get_post_types(cls):
        return cls.POST_TYPE_CHOICES
    
