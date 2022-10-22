import imp
from django.shortcuts import render

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

from .permissions import UpdateOwnUserInfo
from .models import User
from .serializers import UserSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """Handles reading, creating, and updating User"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnUserInfo, )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and reurns an auth token"""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken to validate and create a token"""

        return ObtainAuthToken().as_view()(request=request._request)