from rest_framework import viewsets
from appLearnDRF.models import *
from appLearnDRF.serializers import *


class AuthGroupViewSet(viewsets.ModelViewSet):
    serializer_class = AuthGroupSerializer
    queryset = AuthGroup.objects.all()


class AuthGroupPermissionsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthGroupPermissionsSerializer
    queryset = AuthGroupPermissions.objects.all()


class AuthPermissionViewSet(viewsets.ModelViewSet):
    serializer_class = AuthPermissionSerializer
    queryset = AuthPermission.objects.all()


class AuthUserViewSet(viewsets.ModelViewSet):
    serializer_class = AuthUserSerializer
    queryset = AuthUser.objects.all()

class AuthUserGroupsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthUserGroupsSerializer
    queryset = AuthUserGroups.objects.all()


class AuthUserUserPermissionsViewSet(viewsets.ModelViewSet):
    serializer_class = AuthUserUserPermissionsSerializer
    queryset = AuthUserUserPermissions.objects.all()


class DjangoAdminLogViewSet(viewsets.ModelViewSet):
    serializer_class = DjangoAdminLogSerializer
    queryset = DjangoAdminLog.objects.all()


class DjangoContentTypeViewSet(viewsets.ModelViewSet):
    serializer_class = DjangoContentTypeSerializer
    queryset = DjangoContentType.objects.all()


class DjangoMigrationsViewSet(viewsets.ModelViewSet):
    serializer_class = DjangoMigrationsSerializer
    queryset = DjangoMigrations.objects.all()


class DjangoSessionViewSet(viewsets.ModelViewSet):
    serializer_class = DjangoSessionSerializer
    queryset = DjangoSession.objects.all()
