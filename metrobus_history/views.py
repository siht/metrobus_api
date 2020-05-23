from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
)
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
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


class MetrobusListByDistrict(RetrieveAPIView):
    queryset = HistoricalPoint.objects.all()
    lookup_field = 'place.district'
    serializer_class = DistrictMetrobusSerializer
