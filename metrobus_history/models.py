from django.db import models


class District(models.Model):
    name = models.CharField(max_length=15)


class Place(models.Model):
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    district = models.ForeignKey('District', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('latitude', 'longitude',)


class Metrobus(models.Model):
    serie = models.CharField(max_length=5)
    where_i_was = models.ManyToManyField(Place, through='HistoricalPoint')


class HistoricalPoint(models.Model):
    metrobus = models.ForeignKey(Metrobus, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField()