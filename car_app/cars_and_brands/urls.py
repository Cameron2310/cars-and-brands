from . import views
from django.urls import path

urlpatterns = [
    path('api/', views.CarAPIView.as_view()),
    path('api/brands/', views.FilterBrandAPIView.as_view()),
    path('api/<str:name>/', views.FilterBrandAPIView.as_view()),
]
