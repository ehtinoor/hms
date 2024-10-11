# metal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('metals/', views.metal_list, name='metal-list'),
    path('metals/<int:pk>/', views.metal_detail, name='metal-detail'),
]
