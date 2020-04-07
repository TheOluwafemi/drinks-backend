from beer_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import url

from .views import CustomObtainAuthToken

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewset)
# router.register('login', views.LoginViewSet, basename='login')

urlpatterns = [
    path(r'', include(router.urls)),
    url(r'^authenticate/', CustomObtainAuthToken.as_view()),
]
