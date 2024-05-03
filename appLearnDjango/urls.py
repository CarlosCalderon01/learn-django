from django.urls import path
# from appLearnDjango.views import views
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]
