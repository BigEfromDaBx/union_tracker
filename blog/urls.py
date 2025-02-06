from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # URL for the blog post list
    path('<slug:slug>/', views.post_detail, name='post_detail'),  # URL for the blog post detail view
]