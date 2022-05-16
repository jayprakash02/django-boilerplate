import graphene

class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Ky be lodu!")

schema = graphene.Schema(query=Query)