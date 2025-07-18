# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/<int:car_id>/', views.detail, name='car_detail'),
    path('about/', views.about, name='about'),
    path('car-announcement/', views.car_announcement, name='car-announcement'),
]
