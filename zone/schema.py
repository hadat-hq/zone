import graphene
import zone.apps.posts.schema as post_schema
import zone.apps.users.schema as user_schema
class Query(user_schema.Query,post_schema.Query,graphene.ObjectType):
    pass
class Mutation(user_schema.Mutation,post_schema.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)