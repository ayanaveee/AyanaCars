from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/<int:car_id>/', views.detail, name='car_detail'),
    path('about/', views.about, name='about'),
    path('car-announcement/', views.car_announcement, name='car-announcement'),
    path('car_update/<int:car_id>/', views.car_update, name='car_update'),
    path('delete_car/<int:car_id>/', views.delete_car, name='delete_car'),
    path('add_car/', views.add_car, name='add_car'),
]
