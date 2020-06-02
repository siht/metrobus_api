import graphene

from graphene_django.types import DjangoObjectType

from .models import District


class DistrictType(DjangoObjectType):
    class Meta:
        model = District


class Query(object):
    all_districts = graphene.List(DistrictType)

    def resolve_all_districts(self, info, **kwargs):
        return District.objects.all()
