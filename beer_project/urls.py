"""beer_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from beer_api import urls
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

admin.autodiscover()

schema_view = get_schema_view(
    openapi.Info(
        title="Drinks API",
        default_version='v1',
        description="Backend for drinks sharing app",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('doc/', schema_view.with_ui('redoc',
                                     cache_timeout=0), name='schema-redoc'),
    path('api/', include('beer_api.urls'))
]
