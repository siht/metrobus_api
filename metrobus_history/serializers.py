from rest_framework import serializers

from .models import (
    District,
    HistoricalPoint,
    Metrobus,
)

__all__ = (
    'DistrictsSerializer',
    'DistrictMetrobusSerializer',
    'MetrobusSerializer',
    'MetrobusesSerializer',
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


class DistrictsSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('name',)


class DistrictMetrobusSerializer(serializers.ModelSerializer):
    district = district = serializers.CharField(source='place.district')
    metrobuses = MetrobusesSerializer(source='metrobus', many=True)
    class Meta:
        model = HistoricalPoint
        fields = ('district', 'metrobuses')