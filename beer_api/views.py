from django.shortcuts import render

from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from beer_api import serializers


from beer_api import models
from beer_api import permissions
from beer_api import serializers

# Create your views here.


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})


# class LoginViewSet(ObtainAuthToken):
#     """Checks email and password and returns an auth token."""

#     serializer_class = AuthTokenSerializer

#     def post(self, request, *args, **kwargs):
#         """Use the ObtainAuthToken APIView to validate and create a token."""
#         Response = ObtainAuthToken().post(request)
#         Response.data['message'] = 'Success'
#         Response.data['status'] = '200'
#         Response.data['user'] = ObtainAuthToken().post(self.request.user)
#         return Response

    # def perform_create(self, serializer):
    #     """Sets the user profile to the logged in user"""
    #     serializer.save(user_profile=self.request.user)


class UserProfileFeedViewset(viewsets.ModelViewSet):
    """Handles creating, reading and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permissions.PostOwnStatus,
        IsAuthenticated
    )

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
