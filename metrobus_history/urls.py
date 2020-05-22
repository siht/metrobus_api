from rest_framework import routers
from .views import MetrobusListRetrieve

__all__ = (
    'urlpatterns',
)

router = routers.SimpleRouter()
router.register('metrobus', MetrobusListRetrieve)

urlpatterns = router.urls
