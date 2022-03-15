from django.urls import path
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import (
    AccountRetreiveUpdateDestroy,
    blackListToken,
    register,
    AccountList
)

app_name='users_api'

urlpatterns = [
    path('', AccountList.as_view(), name='list'),
    path('register', register, name='register'), 
    path('logout/blacklist', blackListToken, name='blacklist'), 
    # path('token', AccountTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:account>', AccountRetreiveUpdateDestroy.as_view(), name='detail'),
]

