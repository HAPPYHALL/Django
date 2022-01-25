from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.base_response, name='first_test'),
    path('first/', views.first_view, name='first_view'),
    path('', include('user.urls')),
    path('', include('tweet.urls')),
]