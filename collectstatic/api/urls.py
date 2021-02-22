from django.urls import path
# from api import views
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api_register/', views.MyView.as_view(), name='MyView'),
    path('api_register/post/', views.LearnView.as_view(), name='LearnView'),
    path('api_register/get/', views.LearnDetailView.as_view(), name='LearnDetailView'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns)