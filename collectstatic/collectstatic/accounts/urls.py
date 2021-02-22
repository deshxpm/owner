from django.urls import path
from accounts import views




urlpatterns = [
    path('', views.user_register, name='user_register'),
    path('accounts/login/', views.user_login, name='user_login'),
    path('accounts/logout/', views.user_logout, name='user_logout'),
]
