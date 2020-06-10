from collections import namedtuple

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import (
    District,
    HistoricalPoint,
    Metrobus,
)
from .serializers import (
    DistrictsSerializer,
    DistrictMetrobusSerializer,
    MetrobusSerializer,
    MetrobusesSerializer,
)

__all__ = (
    'DistrictList',
    'MetrobusListRetrieve',
    'MetrobusListByDistrict',
)


class MetrobusListRetrieve(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    lookup_field = 'serie'
    queryset = Metrobus.objects.all()
    serializers = {
        'retrieve': MetrobusSerializer,
        'list': MetrobusesSerializer,
    }

    def get_serializer(self, *args, **kwargs):
        serializer_class =  self.serializers.get(self.action, MetrobusesSerializer)
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class DistrictList(ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictsSerializer


class MetrobusListByDistrict(APIView):
    def get_queryset(self):
        return HistoricalPoint.objects.all()

    def get(self, request, pk, format=None):
        district_name = District.objects.get(pk=pk).name
        what_metrobuses_was_in_certain_district = (
            self.get_queryset()
            .filter(place__district__id=pk)
            .values('metrobus__serie', 'date_time')
        )
        MetrobusesOnDistrict = namedtuple(
            'MetrobusesOnDistrict',
            'district history'
        )
        metrobuses_on_district = MetrobusesOnDistrict(
            district=district_name,
            history=what_metrobuses_was_in_certain_district
        )
        serialized_data = DistrictMetrobusSerializer(metrobuses_on_district)
        return Response(serialized_data.data)
