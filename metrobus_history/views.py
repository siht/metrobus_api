from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from .models import Metrobus
from .serializers import (
    MetrobusSerializer,
    MetrobusesSerializer,
)

__all__ = (
    'MetrobusListRetrieve',
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
