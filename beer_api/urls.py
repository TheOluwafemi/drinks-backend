from beer_api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewset)
router.register('login', views.LoginViewSet, basename='login')

urlpatterns = [
    path(r'', include(router.urls))
]
