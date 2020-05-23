from django.test import TestCase
from django.db.utils import IntegrityError
from django.utils.timezone import now
from rest_framework.test import APIRequestFactory

from .models import (
    District,
    Place,
    Metrobus,
    HistoricalPoint,
)


class ModelsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        district_alvaro_obregon = District.objects.create(name='Álvaro Obregón')
        district_alvaro_obregon.save()
        district_cuauhtemoc = District.objects.create(name='Buena Vista')
        district_cuauhtemoc.save()
        metrobus1 = Metrobus.objects.create(serie='00001')
        metrobus1.save()
        metrobus2 = Metrobus.objects.create(serie='00002')
        metrobus2.save()
        metrobus3 = Metrobus.objects.create(serie='00003')
        metrobus3.save()
        place_in_alvaro_obregon = Place.objects.create(
            latitude=19.347574,
            longitude=-99.187316,
            district=district_alvaro_obregon
        )
        place_in_alvaro_obregon.save()
        place_in_cuauhtemoc = Place.objects.create(
            latitude=19.439686,
            longitude=-99.155558,
            district=district_cuauhtemoc
        )
        place_in_cuauhtemoc.save()
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
            place=place_in_cuauhtemoc,
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


class ViewsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        district_alvaro_obregon = District.objects.create(name='Álvaro Obregón')
        district_alvaro_obregon.save()
        district_cuauhtemoc = District.objects.create(name='Cuauhtémoc')
        district_cuauhtemoc.save()
        district_tlalpan = District.objects.create(name='Tlalpan')
        district_tlalpan.save()
        metrobus1 = Metrobus.objects.create(serie='00001')
        metrobus1.save()
        metrobus2 = Metrobus.objects.create(serie='00002')
        metrobus2.save()
        metrobus3 = Metrobus.objects.create(serie='00003')
        metrobus3.save()
        place_in_alvaro_obregon = Place.objects.create(
            latitude=19.347574,
            longitude=-99.187316,
            district=district_alvaro_obregon
        )
        place_in_alvaro_obregon.save()
        place_in_cuauhtemoc = Place.objects.create(
            latitude=19.439686,
            longitude=-99.155558,
            district=district_cuauhtemoc
        )
        place_in_cuauhtemoc.save()
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
            place=place_in_cuauhtemoc,
            date_time=now()
        )
        history.save()

    def test_metrobus_list(self):
        response = self.client.get('/api/metrobus/')
        self.assertEqual(
            response.data,
            [{'serie': '00001'}, {'serie': '00002'}, {'serie': '00003'}]
        )

    def test_metrobus_detail(self):
        response = self.client.get('/api/metrobus/1/')
        del(response.data['history'][0]['date_time'])
        from collections import OrderedDict
        place_data = OrderedDict()
        place_data['latitude'] = '19.347574'
        place_data['longitude'] = '-99.187316'
        place_data['district'] = 'Álvaro Obregón'
        self.assertEqual(
            response.data,
            {
                'serie': '00001',
                'history': [place_data]
            }
        )