from django.urls import path
from .views import *  # Import all views from views.py

urlpatterns = [
    path('', home, name='home'),  # Home route
    path('index.html', home, name='home'),  # Home route
    path('members.html', member_list, name='member_list'),  # Members list route
    path('member/<int:id>/', member_detail, name='member_detail'),  # Member detail route
]