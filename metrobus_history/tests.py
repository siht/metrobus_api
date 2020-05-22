from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.timezone import now

from .models import (
    District,
    Place,
    Metrobus,
    HistoricalPoint,
)


class ModelsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        district1 = District.objects.create(name='Álvaro Obregón')
        district1.save()
        district2 = District.objects.create(name='Buena Vista')
        district2.save()
        metrobus1 = Metrobus.objects.create(serie='00001')
        metrobus1.save()
        metrobus2 = Metrobus.objects.create(serie='00002')
        metrobus2.save()
        metrobus3 = Metrobus.objects.create(serie='00003')
        metrobus3.save()
        place_in_alvaro_obregon = Place.objects.create(
            latitude=19.347574,
            longitude=-99.187316,
            district=district1
        )
        place_in_alvaro_obregon.save()
        place_in_buena_vista = Place.objects.create(
            latitude=19.439686,
            longitude=-99.155558,
            district=district2
        )
        place_in_buena_vista.save()
        history = HistoricalPoint(
            metrobus=metrobus1,
            place=place_in_alvaro_obregon,
            date_time=now()
        )
        history.save()
        history = HistoricalPoint(
            metrobus=metrobus2,
            place=place_in_alvaro_obregon,
            date_time=now()
        )
        history.save()
        history = HistoricalPoint(
            metrobus=metrobus3,
            place=place_in_buena_vista,
            date_time=now()
        )
        history.save()

    def test_can_get_metrobus_with_district(self):
        district_alvaro_obregon = District.objects.get(name='Álvaro Obregón')
        metrobuses_over_alvaro_obregon = (
            HistoricalPoint
            .objects
            .filter(place__district__id=district_alvaro_obregon.id)
            .values('metrobus__serie', 'date_time')
        )
        self.assertEquals(metrobuses_over_alvaro_obregon.count(), 2)

    def test_can_get_districts_with_metrobus_serie(self):
        metrobus_00001 = Metrobus.objects.get(serie='00001')
        history = (
            metrobus_00001
            .where_i_was
            .values(
                'latitude',
                'longitude',
                'district__name',
                'historicalpoint__date_time'
            )
        )
        self.assertEquals(history.count(), 1)
