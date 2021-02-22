from django.urls import path
from lamp import views


urlpatterns = [
    # path('', views.home, name='homepage'),
    path('integration/', views.integration, name='integration'),
]