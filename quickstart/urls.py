from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register('usuariosDRF', UserViewSet, 'usuariosDRF')

urlpatterns = router.urls
