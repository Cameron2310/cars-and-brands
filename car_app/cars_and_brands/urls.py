from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.UserAPIView.as_view()),
    path('', views.CarAPIView.as_view()),
    path('<int:id>/', views.FilterCarAPIView.as_view()),
    path('brands/', views.FilterBrandAPIView.as_view()),
    path('<str:name>/', views.FilterBrandAPIView.as_view()),
]
