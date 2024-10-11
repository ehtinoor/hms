# myworld/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect

# Create a simple view to handle the root URL
def home(request):
    return HttpResponse("Welcome to the MyWorld API. Go to /api/metals/ for the Metal API.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('metal.urls')),  # Include API URLs
    path('', home),  # Handle the root URL
]
