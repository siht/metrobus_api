from django.urls import path
from rest_framework import routers
from .views import (
    DistrictList,
    MetrobusListRetrieve,
    MetrobusListByDistrict,
)

__all__ = (
    'urlpatterns',
)


router = routers.SimpleRouter()
router.register('metrobus', MetrobusListRetrieve)

urlpatterns = router.urls
urlpatterns += [
    path('district/', DistrictList.as_view()),
    path('district/<int:pk>', MetrobusListByDistrict.as_view()),
]
