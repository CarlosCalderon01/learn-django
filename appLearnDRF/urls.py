from rest_framework import routers
from appLearnDRF.views import *

router = routers.DefaultRouter()

router.register('AuthGroup', AuthGroupViewSet, 'AuthGroup')
router.register('AuthGroupPermissions', AuthGroupPermissionsViewSet, 'AuthGroupPermissions')
router.register('AuthPermission', AuthPermissionViewSet, 'AuthPermission')
router.register('AuthUser', AuthUserViewSet, 'AuthUser')
router.register('AuthUserGroups', AuthUserGroupsViewSet, 'AuthUserGroups')
router.register('AuthUserUserPermissions', AuthUserUserPermissionsViewSet, 'AuthUserUserPermissions')
router.register('DjangoAdminLog', DjangoAdminLogViewSet, 'DjangoAdminLog')
router.register('DjangoContentType', DjangoContentTypeViewSet, 'DjangoContentType')
router.register('DjangoMigrations', DjangoMigrationsViewSet, 'DjangoMigrations')
router.register('DjangoSession', DjangoSessionViewSet, 'DjangoSession')

urlpatterns = router.urls
