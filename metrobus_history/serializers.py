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
    district = serializers.CharField(source='place.district')
    latitude = serializers.DecimalField(
        source='place.latitude',
        max_digits=9,
        decimal_places=6
    )
    longitude = serializers.DecimalField(
        source='place.longitude',
        max_digits=9,
        decimal_places=6
    )
    class Meta:
        model = HistoricalPoint
        fields = ('latitude', 'longitude', 'date_time', 'district')


class MetrobusSerializer(serializers.ModelSerializer):
    history = HistorySerializer(
        source='historicalpoint_set',
        many=True
    )

    class Meta:
        model = Metrobus
        fields = ('serie', 'history',)
