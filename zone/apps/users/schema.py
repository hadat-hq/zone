import graphene
from django.contrib.auth import get_user_model
from zone.apps.users.types import (
    UserType
)

class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info, **kwargs):
        return get_user_model().objects.all()

class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)
    
    def mutate(self, info,username, email, password):
        user = get_user_model() (
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save()

        return CreateUser(user=user)
    
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()