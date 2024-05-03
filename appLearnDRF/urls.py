from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('usuariosDRF', UserClientViewSet, 'usuariosDRF')

urlpatterns = router.urls