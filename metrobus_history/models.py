from django.db import models

__all__ = (
    'District',
    'Place',
    'Metrobus',
    'HistoricalPoint',
)


class District(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Place(models.Model):
    latitude = models.DecimalField(max_digits=14, decimal_places=12)
    longitude = models.DecimalField(max_digits=15, decimal_places=12)
    district = models.ForeignKey(
        'District',
        null=True,
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = ('latitude', 'longitude',)
    
    def __str__(self):
        dist = self.district and self.district or 'N/D'
        return '({lat}, {lon}) on district: {dist}'.format(
            lat=self.latitude,
            lon=self.longitude,
            dist=dist
        )


class Metrobus(models.Model):
    serie = models.CharField(max_length=5, unique=True)
    where_i_was = models.ManyToManyField(Place, through='HistoricalPoint')

    def __str__(self):
        return self.serie


class HistoricalPoint(models.Model):
    metrobus = models.ForeignKey(Metrobus, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return '{metrobus} in {place} at {dt}'.format(
            metrobus=self.metrobus,
            place=self.place,
            dt=self.date_time
        )
