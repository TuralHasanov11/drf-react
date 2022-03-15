
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('users.api.urls'), name='users_api'),


]
