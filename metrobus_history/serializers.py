from rest_framework import serializers

from .models import Metrobus, HistoricalPoint

__all__ = (
    'MetrobusesSerializer',
    'MetrobusSerializer',
)

class MetrobusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrobus
        fields = ('serie',)


class HistorySerializer(serializers.ModelSerializer):
    district = serializers.CharField(source='district__name')

    class Meta:
        model = HistoricalPoint
        fields = ('longitude', 'latitude', 'date_time', 'district__name')


class MetrobusSerializer(serializers.ModelSerializer):
    history = HistorySerializer(
        source='where_i_was',
        many=True,
        read_only=True
    )

    class Meta:
        model = Metrobus
        fields = ('serie', 'where_i_was')
