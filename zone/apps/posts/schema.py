import graphene
from zone.apps.posts.types import (
    ForumType,
    PostType
)
from zone.apps.posts.models import (
    Forum,
    Post
)

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    forums = graphene.List(ForumType)

    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()
    def resolve_forums(self, info, **kwargs):
        return Forum.objects.all()

class CreatePost(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        post_type = graphene.String()
        title = graphene.String()
        content = graphene.String(required=False)
        media_url = graphene.String(required=False)
        media_type = graphene.String(required=False)
        url = graphene.String(required=False)
        forum = graphene.Int()

    def mutate(self, info, post_type, title, forum, media_url=None, content=None, media_type=None, url=None):
        post = None
        if not title:
            raise Exception("Title field required")
        
        if not content and not media_type and not url:
            raise Exception("One of the fields required (content, media,  url)")
        if not forum:
            raise Exception("Forum required")
        forum = Forum.objects.get(pk=forum)
        if not forum:
            raise Exception(f"Forum with id {forum} not found")
        if content:
            post = Post(title=title, content=content, forum=forum)
        elif media_type and media_url:
            post = Post(title=title, media_url=media_url, media_type=media_type, forum=forum)
        elif url:
            post = Post(title=title, url=url, forum=forum)
        else:
            data_dict = {
                'title': title,
                'content': content,
                'url': url,
                'media_url': media_url,
                'media_type': media_type,
                'forum_id': lambda: forum if type(forum) == int else forum.name
            }
            raise Exception(f"Error processing data {data_dict}")
        if not post:
            raise Exception("Error post is None")
        if not post_type:
            raise Exception("Post type required")
        post.post_type = post_type
        post.save()

        return CreatePost(
            post = post
        )
class CreateForum(graphene.Mutation):
    forum = graphene.Field(ForumType)

    class Arguments:
        explicit = graphene.Boolean(required=True)
        name = graphene.String(required=True)
        community_type = graphene.String(required=True)
    
    def mutate(self, info, name, community_type, explicit, **kwargs):
        t = Forum.get_forum_types()
        valid = False
        for a in t:
            if community_type == a[0] or community_type == a[1]:
                if community_type == a[1]:
                    community_type = a[0]
                valid = True
        if valid:
            forum = Forum(name=name, community_type=community_type, explicit=explicit)
            forum.save()
        else:
            raise Exception("Invalid Community Type")
        return CreateForum(
            forum=forum
        )
class Mutation(graphene.ObjectType):
    create_post = CreatePost.Field()
    create_forum = CreateForum.Field()