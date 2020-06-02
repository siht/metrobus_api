import graphene

from graphene_django.debug import DjangoDebug

import metrobus_history.schema


class Query(
        metrobus_history.schema.Query,
        graphene.ObjectType
    ):
    debug = graphene.Field(DjangoDebug, name="_debug")


schema = graphene.Schema(query=Query)
