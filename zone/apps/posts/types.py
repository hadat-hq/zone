from graphene_django import DjangoObjectType
from zone.apps.posts.models import (
    Forum,
    Post
)

class ForumType(DjangoObjectType):
    class Meta:
        model = Forum
class PostType(DjangoObjectType):
    class Meta:
        model = Post