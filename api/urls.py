from django.urls import path
from api import views


urlpatterns = [
    path('api_register/', views.api_register, name='api_register'),
]