from django.shortcuts import render

from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from quickstart.serializers import GroupSerializer, UserSerializer

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #
# ///// # ///// # TITULAR: Tutorial quickstart
# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #
# ///// # ///// # TITULAR: Tutorial quickstart
# ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- # ----- #

"""

- Bibliografia extra opcional:

- metodo antiguo:
    https://www.django-rest-framework.org/api-guide/views/

- para vistas mas comunes:
    https://www.django-rest-framework.org/api-guide/generic-views/

- todos los metodos en uno:
    https://www.django-rest-framework.org/api-guide/viewsets/

"""