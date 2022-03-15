from django.http import request
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import  BasePermission,IsAuthenticated,IsAuthenticatedOrReadOnly, SAFE_METHODS, AllowAny
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView  
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import viewsets

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import Account
from .serializers import RegistrationSerializer, AccountSerializer
from .pagination import AccountPagination



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def register(request):

    serializer = RegistrationSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        return Response(status=status.HTTP_201_CREATED)
        

@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def blackListToken(request):
    try:
        refreshToken = request.data['refresh_token']
        token = RefreshToken(refreshToken)
        token.blacklist()
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    return Response({'message':'refresh token blacklisted'})

    
class AccountList(ListAPIView):
    permission_classes=[]
    authentication_classes=[]
    serializer_class = AccountSerializer
    pagination_class = AccountPagination
    search_fields = ['username', 'email']
    ordering_fields = ['username', 'email']
    ordering = ['username']
    filter_backends = [SearchFilter,OrderingFilter]

    def get_queryset(self):
        return Account.objects.all()


class AccountWritePermission(BasePermission):

    def has_permission(self, request, view):
        self.message = 'You are not allowed to modify the account'
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        self.message = 'You are not allowed to modify the account'
        if obj == request.user:
            return True
        else:
            return False


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS

class AccountRetreiveUpdateDestroy(RetrieveUpdateDestroyAPIView):

    permission_classes = [ReadOnly|AccountWritePermission]
    serializer_class = AccountSerializer

    def get_queryset(self):
        return Account.objects.all()

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), id=self.kwargs['account'])
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     try:
#         user = request.user
#     except Account.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     serializer = ProfileSerializer(user)
#     return Response(serializer.data)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def profileUpdate(request):
#     try:
#         user = request.user
#     except Account.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    
#     serializer = ProfileSerializer(user, data=request.data)

#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
        
#         return Response({'message':'Profile updated'})
    
#     return Response({'message':'Failed'}, status.HTTP_400_BAD_REQUEST)


# @api_view(['GET'])
# @permission_classes([])
# def accountDetail(request, id):
#     try:
#         account = Account.objects.get(id=id)
#     except Account.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     serializer = AccountSerializer(account)
#     return Response(serializer.data)
    


class AccountTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token

class AccountTokenObtainPairView(TokenObtainPairView):
    serializer_class = AccountTokenObtainPairSerializer