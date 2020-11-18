from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls', namespace='employee')),
    path('api/', include('manager_Api.urls', namespace='manager_Api')),
    path('api/user/', include('users.urls', namespace='users')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('payments/', include('payments.urls')),
    path('docs/', include_docs_urls(title='managerapp')),
    path('schema', get_schema_view(
        title="ManagerApp",
        description="API for the ManagerApp",
        version="1.0.0"
    ), name='openapi-schema'),
]
