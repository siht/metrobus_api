import graphene

from graphene_django.types import DjangoObjectType

from .models import (
    District,
    Metrobus,
)


class DistrictType(DjangoObjectType):
    class Meta:
        model = District


class MetrobusType(DjangoObjectType):
    class Meta:
        model = Metrobus


class Query(object):
    all_districts = graphene.List(DistrictType)
    all_metrobuses = graphene.List(MetrobusType)

    def resolve_all_districts(self, info, **kwargs):
        return District.objects.all()

    def resolve_all_metrobuses(self, info, **kwargs):
        return Metrobus.objects.all()