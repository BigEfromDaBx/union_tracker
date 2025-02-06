from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView


admin.site.site_header = 'Local947.org'
admin.site.site_title = 'Local947.org'
admin.site.index_title = 'Local947.org Admin'



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', RedirectView.as_view(url='https://google.com')),  # Redirect to an external URL
    path('', include('members.urls')),  # Assuming you have other URLs here
]