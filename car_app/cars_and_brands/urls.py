from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('<int:id>/', views.brand_details, name='brand_details'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/edit/update/', views.update_record, name='update_record'),
    path('<int:brand_id>/cars/', views.cars, name="cars"),
    path('<int:brand_id>/cars/new/', views.new_car, name="new_car"),
    path('<int:brand_id>/cars/<int:car_id>/', views.car_details),
    path('<int:brand_id>/cars/<int:car_id>/edit/',
         views.edit_car, name='edit_cars'),
    path('<int:brand_id>/cars/<int:car_id>/edit/update',
         views.update_car_record, name='update_car_record')
]
